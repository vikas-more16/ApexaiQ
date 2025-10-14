from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

urls = ["https://versionsof.net/core/8.0/8.0.0/"]

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

all_data = []

for url in urls:
    print(f"\nScraping: {url}")
    driver.get(url)

    try:
        tables = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))
        print(f"   Found {len(tables)} tables.")

        for i, table in enumerate(tables, start=1):
            headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]
            rows = table.find_elements(By.TAG_NAME, "tr")
            print(f"   Table {i} - {len(rows)-1} rows.")

            for row in rows[1:]:
                cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
                if not cells:
                    continue

                version = cells[0]
                version_name = " | ".join(headers) if headers else "Unknown"
                versions = [v.strip() for v in version.split(",") if v.strip()]

                for v in versions:
                    all_data.append({
                        "Table": f"Table {i}",
                        "Version Name": version_name,
                        "Version": v,
                        "URL": url,
                    })

    except Exception as e:
        print(f"No tables found - {e}")

driver.quit()

df = pd.DataFrame(all_data)
df.to_csv("core_8_0_0.csv", index=False, encoding='utf-8-sig')

print(f"\nDone! Total {len(df)} rows saved to all_tables_versions.csv")
