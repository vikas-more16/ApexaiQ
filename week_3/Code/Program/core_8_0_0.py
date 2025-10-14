"""
Selenium Web Scraping Script: Scrape Multiple Tables from a Webpage

This script scrapes two tables from the given URL and saves them into a single CSV file.
- Adds the table name as a header row before each table.
- Adds a blank row to separate tables.
- Adds the current date as 'Scraped Date' for each row.

Requirements:
- selenium
- pandas
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# -------------------------
# Configuration
# -------------------------

URL = "https://versionsof.net/core/8.0/8.0.0/"
OUTPUT_FOLDER = "./week_3/Code/Output/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Create folder if it doesn't exist

# Tables to scrape with their XPaths and friendly names
TABLES_INFO = [
    {"xpath": "(//table)[1]", "name": "Download Table"},
    {"xpath": "(//table)[2]", "name": "Updated Packages"}
]

# Get current date for 'Scraped Date' column
today = pd.Timestamp.now().strftime("%d-%m-%Y")

# -------------------------
# Start WebDriver
# -------------------------
driver = webdriver.Chrome()
driver.get(URL)

# -------------------------
# Scraping Logic
# -------------------------
all_rows = []  # Store all table rows

for table_info in TABLES_INFO:
    try:
        # Wait until table is present
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, table_info["xpath"]))
        )

        # Extract headers
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

        # Add table name as a row
        all_rows.append({headers[0]: table_info["name"]})

        # Extract data rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows[1:]:  # Skip the header row
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cells:
                # Map headers to cells, add 'Scraped Date'
                row_data = {headers[j]: cells[j] if j < len(cells) else "" for j in range(len(headers))}
                row_data["Scraped Date"] = today
                all_rows.append(row_data)

        # Add blank row to separate tables
        all_rows.append({})

    except Exception as e:
        print(f"Error scraping {table_info['name']}: {e}")

# -------------------------
# Close WebDriver
# -------------------------
driver.quit()

# -------------------------
# Convert to DataFrame and Save CSV
# -------------------------
df = pd.DataFrame(all_rows)
output_file = os.path.join(OUTPUT_FOLDER, "core_8_0_0_all_tables.csv")
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"Both tables saved successfully to {output_file}")
