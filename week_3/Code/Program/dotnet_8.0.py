from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

# 1) Setup Chrome
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
    # 2) Go to the page
    driver.get("https://dotnet.microsoft.com/en-us/download/dotnet/8.0")

    # 3) Wait for JS content to fully load
    time.sleep(8)  # Give time for dynamic React content to render

    # 4) Extract all links that contain "download" or "dotnet"
    links = driver.find_elements(By.TAG_NAME, "a")

    data = []
    for link in links:
        href = link.get_attribute("href")
        text = link.text.strip()
        if href and ("dotnet" in href or "download" in href):
            data.append({
                "Link Text": text,
                "URL": href
            })

    # 5) Save to CSV
    if data:
        df = pd.DataFrame(data)
        df.to_csv("dotnet_8.0.csv", index=False)
        print("Saved: dotnet_8.0.csv with", len(df), "rows.")
    else:
        print("No download links found.")

finally:
    driver.quit()
