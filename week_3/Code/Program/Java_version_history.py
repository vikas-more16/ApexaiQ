from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# 1) Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

def split_multi(cell_text):
    """Split multiple values in a cell (by / or ,)."""
    parts = re.split(r"\s*/\s*|\s*,\s*", cell_text.strip())
    return [p for p in parts if p]

def expand_rows_for_multivals(headers, rows):
    """Recursively expand rows if any cell has multiple values."""
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
    # Check again if any row still has multi-values
    need_more = any(len(split_multi(r[h])) > 1 for r in expanded for h in headers)
    if need_more:
        return expand_rows_for_multivals(headers, expanded)
    return expanded

try:
    # 2) Go to the page
    driver.get("https://en.wikipedia.org/wiki/Java_version_history")

    # 3) Wait until at least one table is present
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.wikitable")))

    # 4) Scrape all wikitable tables
    all_rows = []
    all_headers = []

    tables = driver.find_elements(By.CSS_SELECTOR, "table.wikitable")

    for tbl in tables:
        # Get headers
        ths = tbl.find_elements(By.TAG_NAME, "th")
        headers = [th.text.strip() for th in ths]
        if not headers:
            continue
        if not all_headers:
            all_headers = headers
        else:
            for h in headers:
                if h not in all_headers:
                    all_headers.append(h)

        # Get rows
        trs = tbl.find_elements(By.TAG_NAME, "tr")
        rows = []
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if not tds:
                continue
            row_texts = [td.text.strip() for td in tds]
            if len(row_texts) != len(headers):
                continue  # skip malformed row
            row = dict(zip(headers, row_texts))
            rows.append(row)

        # Expand multiple values in cells
        rows_expanded = expand_rows_for_multivals(headers, rows)

        # Normalize rows with all_headers
        for r in rows_expanded:
            for h in all_headers:
                if h not in r:
                    r[h] = ""
            all_rows.append(r)

    # 5) Make a DataFrame and save
    df = pd.DataFrame(all_rows)
    print(df.head())
    df.to_csv("java_version_history.csv", index=False)

finally:
    driver.quit()
