from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import re
import os

URL = "https://www.dbf2002.com/news.html"
OUTPUT_FOLDER = "./week_3/Code/Output/"
OUTPUT_FILE = "dbf2002.csv"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  
driver = webdriver.Chrome()
driver.get(URL)
data =[]

try: 
    h3_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//h3")
        )
    )
    for h3 in h3_elements:

        text = h3.text.strip()

        version_match = re.search(r"(v[^\s]+)", text)
        version = version_match.group(1) if version_match else None

        date_match = re.search(r"\(([^)]+)\)", text)
        date_str = date_match.group(1) if date_match else None

        formatted_date = None
        if date_str:
            try:
                date_obj = datetime.strptime(date_str, "%B %d, %Y")
                formatted_date = date_obj.strftime("%m/%d/%y")
            except ValueError:
                formatted_date = "Invalid Date"
        print(f"Version: {version} | Date: {formatted_date}")

        data.append({
        "Version": version,
        "Date": formatted_date,
        "URL": URL
        })

    df = pd.DataFrame(data)

    df.to_csv(os.path.join(OUTPUT_FOLDER, OUTPUT_FILE), index=False, encoding="utf-8-sig")
    print(f"Table scraped successfully and saved as {OUTPUT_FILE}!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
