from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# --- Configuration ---
URL = "https://learn.microsoft.com/en-us/windows/release-health/windows-server-release-info"
OUTPUT_FOLDER = "./week_3/Code/Output/"
OUTPUT_FILE = "windows_server_release_info.csv"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  

today = pd.Timestamp.now().strftime("%d-%m-%Y")

# --- Initialize WebDriver ---
driver = webdriver.Chrome()
driver.get(URL)

all_data = []  # Store final CSV rows

try:
    # Wait for all tables on the page
    tables = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table"))
    )

    for idx, table in enumerate(tables):
        # Extract headers
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

        # If no <th> headers, use first row as headers
        if not headers:
            first_row = table.find_elements(By.TAG_NAME, "tr")[0]
            headers = [td.text.strip() for td in first_row.find_elements(By.TAG_NAME, "td")]

        num_headers = len(headers)
        if num_headers == 0:
            continue  # skip empty tables

        # --- Add header row to CSV ---
        all_data.append({headers[i]: headers[i] for i in range(num_headers)})

        # Extract table rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        start_index = 1 if table.find_elements(By.TAG_NAME, "th") else 1
        for row in rows[start_index:]:
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cells:
                # Pad cells to match headers
                while len(cells) < num_headers:
                    cells.append("")
                row_data = {headers[i]: cells[i] for i in range(num_headers)}
                row_data["Scraped Date"] = today
                all_data.append(row_data)

        # Add a blank row to separate tables
        all_data.append({})

except Exception as e:
    print("Error scraping tables:", e)

finally:
    driver.quit()

# Convert to DataFrame and save CSV
df = pd.DataFrame(all_data)
output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"All tables scraped successfully and saved to {output_path}")
