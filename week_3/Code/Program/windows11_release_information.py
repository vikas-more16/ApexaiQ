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
    url = "https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information"
    driver.get(url)

    # Wait until table or key content loads
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table, h2, h3, div[data-role='table']")))

    all_rows = []
    all_headers = []

    # Scrape all <table> elements
    tables = driver.find_elements(By.TAG_NAME, "table")
    for tbl in tables:
        ths = tbl.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in ths]
        if not headers:
            continue
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
            rows.append(dict(zip(headers, vals)))

        rows_expanded = expand_rows_for_multivals(headers, rows)
        for r in rows_expanded:
            for h in all_headers:
                if h not in r:
                    r[h] = ""
            all_rows.append(r)

    # Capture headings or section titles, if needed
    headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
    heading_texts = [h.text.strip() for h in headings if h.text.strip()]

    # Put headings in first row as metadata
    if all_rows:
        all_rows[0]["Page_Headings"] = " | ".join(heading_texts)
    else:
        all_rows = [{"Page_Headings": " | ".join(heading_texts)}]
        all_headers = ["Page_Headings"]

    if "Page_Headings" not in all_headers:
        all_headers.append("Page_Headings")
    for r in all_rows:
        if "Page_Headings" not in r:
            r["Page_Headings"] = ""

    df = pd.DataFrame(all_rows, columns=all_headers)
    fname = clean_filename("windows11_release_information") + ".csv"
    df.to_csv(fname, index=False)
    print("Saved:", fname, " rows:", len(df))

finally:
    driver.quit()
