from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Java_version_history")


try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@class='wikitable sticky-header']"))
    )
    
    headers = [th.text.strip() for th in table.find_elements(By.XPATH, ".//th")]
    
    rows = table.find_elements(By.XPATH, ".//tr")
    data = []

    for row in rows[1:]:
        cells = [td.text.strip() for td in row.find_elements(By.XPATH, ".//td")]
        if cells:
            data.append(cells)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)
    output_folder = "./week_3/Code/Output/"
    os.makedirs(output_folder, exist_ok=True)
    df.to_csv(os.path.join(output_folder, "java_version_history.csv"), index=False, encoding="utf-8-sig")
    print("Table scraped successfully and saved as CSV!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
