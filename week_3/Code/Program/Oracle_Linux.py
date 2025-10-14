from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# --- Configuration ---
URL = "https://en.wikipedia.org/wiki/Oracle_Linux"
OUTPUT_FOLDER = "./week_3/Code/Output/"
OUTPUT_FILE = "Oracle_Linux.csv"

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  

# --- Initialize WebDriver ---
driver = webdriver.Chrome()
driver.get(URL)

# --- Function to extract table data ---
def extract_table_data(table):
    headers = [th.text.strip() for th in table.find_elements(By.XPATH, ".//th")]
    num_headers = len(headers)
    rows = table.find_elements(By.XPATH, ".//tr")
    data = []

    for row in rows[1:]:  # Skip header row
        cells = [td.text.strip() for td in row.find_elements(By.XPATH, ".//td")]
        if cells:
            # Pad missing cells to match headers
            while len(cells) < num_headers:
                cells.append("")
            data.append(cells)

    return pd.DataFrame(data, columns=headers)

try:
    # Wait for all tables containing 'wikitable' in class
    tables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table[contains(@class, 'wikitable')]"))
    )

    all_data = []  # Store all tables here

    for idx, table in enumerate(tables):
        df_table = extract_table_data(table)

        # Add table title row
        df_table.loc[-1] = [f"Table {idx + 1}"] + [""] * (df_table.shape[1] - 1)
        df_table.index = df_table.index + 1
        df_table = df_table.sort_index()

        # Append table and a blank row for separation
        all_data.append(df_table)
        all_data.append(pd.DataFrame([[""] * df_table.shape[1]], columns=df_table.columns))

    # Combine all tables into one DataFrame
    final_df = pd.concat(all_data, ignore_index=True, sort=False)

    # Save to CSV
    final_df.to_csv(os.path.join(OUTPUT_FOLDER, OUTPUT_FILE), index=False, encoding="utf-8-sig")
    print(f"All tables scraped successfully and saved as {OUTPUT_FILE}!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
