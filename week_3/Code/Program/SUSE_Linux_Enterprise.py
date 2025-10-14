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
    return re.sub(r"[^0-9a-zA-Z_]+", "_", s)

try:
    url = "https://en.wikipedia.org/wiki/SUSE_Linux_Enterprise"
    driver.get(url)

    # Wait until the main content loads
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mw-parser-output")))

    # 1) Page title
    title = driver.title

    # 2) Introduction (first paragraph under content)
    intro = ""
    try:
        intro_elem = driver.find_element(By.CSS_SELECTOR, "div.mw-parser-output > p")
        intro = intro_elem.text.strip()
    except Exception as e:
        pass

    # 3) Infobox data
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

    # 4) Scrape wikitable tables
    all_headers = []
    all_rows = []
    tables = driver.find_elements(By.CSS_SELECTOR, "table.wikitable")
    for tbl in tables:
        ths = tbl.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in ths]
        if not headers:
            continue
        # collect headers globally
        for h in headers:
            if h not in all_headers:
                all_headers.append(h)

        trs = tbl.find_elements(By.TAG_NAME, "tr")
        rows = []
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if not tds:
                continue
            vals = [td.text.strip() for td in tds]
            if len(vals) != len(headers):
                continue
            row_dict = dict(zip(headers, vals))
            rows.append(row_dict)

        rows_expanded = expand_rows_for_multivals(headers, rows)
        for r in rows_expanded:
            # fill missing headers
            for h in all_headers:
                if h not in r:
                    r[h] = ""
            all_rows.append(r)

    # 5) Merge page-level info into each row (or fallback row)
    if not all_rows:
        # no table data, create a row with page-level info
        row = {"Title": title, "Introduction": intro}
        for k, v in infobox_data.items():
            row[k] = v
        all_rows = [row]
        all_headers = list(row.keys())
    else:
        for r in all_rows:
            r["Page_Title"] = title
            r["Introduction"] = intro
            for k, v in infobox_data.items():
                r[k] = v
        for extra in ["Page_Title", "Introduction"] + list(infobox_data.keys()):
            if extra not in all_headers:
                all_headers.append(extra)

    # 6) Save to CSV
    df = pd.DataFrame(all_rows, columns=all_headers)
    fname = clean_filename("SUSE_Linux_Enterprise") + ".csv"
    df.to_csv(fname, index=False)
    print("Saved:", fname, " — rows:", len(df))

finally:
    driver.quit()
