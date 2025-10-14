from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# 1) Setup Chrome / Selenium
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
            vals = split_multi(row[h])
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
    need_more = any(len(split_multi(r[h])) > 1 for r in expanded for h in headers)
    if need_more:
        return expand_rows_for_multivals(headers, expanded)
    return expanded

try:
    url = "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info"
    driver.get(url)

    # Wait until a table or content is loaded
    wait = WebDriverWait(driver, 20)
    # We wait for any table or headings to show
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table, h2, h3")))

    all_rows = []
    all_headers = []

    # Scrape all <table> tags
    tables = driver.find_elements(By.TAG_NAME, "table")
    for tbl in tables:
        # headers
        ths = tbl.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in ths]
        if not headers:
            continue
        if not all_headers:
            all_headers = headers.copy()
        else:
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
            row_texts = [td.text.strip() for td in tds]
            # if mismatch lengths, skip
            if len(row_texts) != len(headers):
                continue
            row = dict(zip(headers, row_texts))
            rows.append(row)

        # expand multi-values
        rows_expanded = expand_rows_for_multivals(headers, rows)

        for r in rows_expanded:
            # fill missing columns
            for h in all_headers:
                if h not in r:
                    r[h] = ""
            all_rows.append(r)

    # Additionally, you may want to capture some heading text or summary paragraphs
    # For example:
    summary = []
    # find h1/h2 headings
    headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
    for h in headings:
        text = h.text.strip()
        if text:
            summary.append(text)
    # we can put summary in first row
    if all_rows:
        all_rows[0]["Page Headings"] = " | ".join(summary)
    else:
        # if there were no tables, create a fallback
        all_rows = [{"Page Headings": " | ".join(summary)}]
        all_headers = ["Page Headings"]

    # Normalize all rows to include "Page Headings" column
    if "Page Headings" not in all_headers:
        all_headers.append("Page Headings")
    for r in all_rows:
        if "Page Headings" not in r:
            r["Page Headings"] = ""

    # Save to CSV
    df = pd.DataFrame(all_rows)
    df.to_csv("windows_server_release_info.csv", index=False)
    print("Saved: windows_server_release_info.csv (rows:", len(df), ")")

finally:
    driver.quit()
