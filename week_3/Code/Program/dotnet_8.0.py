from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

URL = "https://dotnet.microsoft.com/en-us/download/dotnet/8.0"
OUTPUT_FOLDER = "./week_3/Code/Output/"
OUTPUT_FILE = "dotnet_8_0.csv"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

driver = webdriver.Chrome()
driver.get(URL)

dataframes = []

try:
    # Wait for all tables to load
    tables = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-sm']"))
    )

    headings =WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h3"))
    )

    for i, table in enumerate(tables):
        table_name = headings[i].text.strip() if i < len(headings) else f"Table {i+1}"
        print(f"Scraping: {table_name}")

        html_content = table.get_attribute("outerHTML")
        df = pd.read_html(html_content)[0]

        name_df = pd.DataFrame([[table_name]], columns=df.columns[:1])
        blank_row = pd.DataFrame([[" "]*len(df.columns)], columns=df.columns)

        dataframes.extend([name_df, df, blank_row])

    final_df = pd.concat(dataframes, ignore_index=True)
    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
    final_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"All tables scraped and saved as {output_path}")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
