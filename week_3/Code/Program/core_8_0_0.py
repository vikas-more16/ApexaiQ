from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

URL = "https://versionsof.net/core/8.0/8.0.0/"
OUTPUT_FOLDER = "./week_3/Code/Output/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  

TABLES_INFO = [
    {"xpath": "(//table)[1]", "name": "Download Table"},
    {"xpath": "(//table)[2]", "name": "Updated Packages"}
]

today = pd.Timestamp.now().strftime("%d-%m-%Y")

driver = webdriver.Chrome()
driver.get(URL)


all_rows = [] 

for table_info in TABLES_INFO:
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, table_info["xpath"]))
        )

        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

        all_rows.append({headers[0]: table_info["name"]})

        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows[1:]: 
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cells:
                row_data = {headers[j]: cells[j] if j < len(cells) else "" for j in range(len(headers))}
                row_data["Scraped Date"] = today
                all_rows.append(row_data)

        all_rows.append({})

    except Exception as e:
        print(f"Error scraping {table_info['name']}: {e}")


driver.quit()

df = pd.DataFrame(all_rows)
output_file = os.path.join(OUTPUT_FOLDER, "core_8_0_0_all_tables.csv")
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"Both tables saved successfully to {output_file}")
