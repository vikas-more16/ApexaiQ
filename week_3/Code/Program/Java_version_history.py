"""
Wikipedia Table Scraping Script: Java Version History

This script scrapes the first 'wikitable sticky-header' table from the
Java version history Wikipedia page and saves it as a CSV file.

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
URL = "https://en.wikipedia.org/wiki/Java_version_history"
OUTPUT_FOLDER = "./week_3/Code/Output/"
OUTPUT_FILE = "java_version_history.csv"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Create folder if not exists

# -------------------------
# Start WebDriver
# -------------------------
driver = webdriver.Chrome()
driver.get(URL)

try:
    # Wait until the table is present
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//table[@class='wikitable sticky-header']")
        )
    )

    # Extract headers
    headers = [th.text.strip() for th in table.find_elements(By.XPATH, ".//th")]

    # Extract table rows
    rows = table.find_elements(By.XPATH, ".//tr")
    data = []

    for row in rows[1:]:  # Skip header row
        cells = [td.text.strip() for td in row.find_elements(By.XPATH, ".//td")]
        if cells:
            data.append(cells)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Save as CSV
    df.to_csv(os.path.join(OUTPUT_FOLDER, OUTPUT_FILE), index=False, encoding="utf-8-sig")
    print(f"Table scraped successfully and saved as {OUTPUT_FILE}!")

except Exception as e:
    print("Error:", e)

finally:
    # Close the WebDriver
    driver.quit()
