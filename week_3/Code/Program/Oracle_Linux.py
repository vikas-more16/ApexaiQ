from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# ---------- 1) Setup Chrome ----------
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

def split_multi(cell_text):
    parts = re.split(r"\s*/\s*|\s*,\s*", cell_text.strip())
    return [p for p in parts if p]

def expand_rows_for_multivals(headers, rows):
    expanded = []
    for row in rows:
        multi_header = None
        multi_values = None
        for h in headers:
            vals = split_multi(row.get(h, ""))
            if len(vals) > 1:
                multi_header = h
                multi_values = vals
                break
        if multi_header is None:
            expanded.append(row)
        else:
            for v in multi_values:
                new_row = dict(row)
                new_row[multi_header] = v
                expanded.append(new_row)
    need_more = any(len(split_multi(r.get(h, ""))) > 1 for r in expanded for h in headers)
    if need_more:
        return expand_rows_for_multivals(headers, expanded)
    return expanded

def clean_filename(s):
    # safe file name from title
    return re.sub(r"[^0-9a-zA-Z_]+", "_", s)

try:
    url = "https://en.wikipedia.org/wiki/Oracle_Linux"
    driver.get(url)

    # wait until page title or content loads
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mw-parser-output")))

    # 1) Get the page title
    title = driver.title  # e.g. "Oracle Linux - Wikipedia"
    # 2) Get first paragraph (intro)
    intro = ""
    try:
        intro_p = driver.find_element(By.CSS_SELECTOR, "div.mw-parser-output > p")
        intro = intro_p.text.strip()
    except:
        pass

    # 3) Scrape infobox (the table on right side)
    infobox_data = {}
    try:
        infobox = driver.find_element(By.CSS_SELECTOR, "table.infobox")
        rows = infobox.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            ths = row.find_elements(By.TAG_NAME, "th")
            tds = row.find_elements(By.TAG_NAME, "td")
            if len(ths) == 1 and len(tds) == 1:
                key = ths[0].text.strip()
                val = tds[0].text.strip()
                infobox_data[key] = val
    except:
        pass

    # 4) Scrape all other wikitable tables
    all_headers = []
    all_rows = []

    tables = driver.find_elements(By.CSS_SELECTOR, "table.wikitable")
    for tbl in tables:
        # headers
        ths = tbl.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in ths]
        if not headers:
            continue
        # extend global headers
        for h in headers:
            if h not in all_headers:
                all_headers.append(h)

        # rows
        trs = tbl.find_elements(By.TAG_NAME, "tr")
        rows = []
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if not tds:
                continue
            row_vals = [td.text.strip() for td in tds]
            if len(row_vals) != len(headers):
                continue
            row_dict = dict(zip(headers, row_vals))
            rows.append(row_dict)

        rows_expanded = expand_rows_for_multivals(headers, rows)
        for r in rows_expanded:
            # fill missing for all_headers
            for h in all_headers:
                if h not in r:
                    r[h] = ""
            all_rows.append(r)

    # 5) If no table rows, create an entry with just title + intro + infobox
    if not all_rows:
        row = {"Title": title, "Intro": intro}
        # add infobox keys
        for k,v in infobox_data.items():
            row[k] = v
        all_rows = [row]
        all_headers = list(row.keys())
    else:
        # put title, intro, infobox as extra columns in each row
        for r in all_rows:
            r["Page_Title"] = title
            r["Introduction"] = intro
            for k,v in infobox_data.items():
                r[k] = v

        # ensure headers include these
        for extra in ["Page_Title", "Introduction"] + list(infobox_data.keys()):
            if extra not in all_headers:
                all_headers.append(extra)

    # 6) Save to CSV
    df = pd.DataFrame(all_rows, columns=all_headers)
    fname = clean_filename("Oracle_Linux") + ".csv"
    df.to_csv(fname, index=False)
    print("Saved:", fname, "rows:", len(df))

finally:
    driver.quit()
