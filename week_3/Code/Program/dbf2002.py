from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
from dateutil import parser as dateparser  # pip install python-dateutil

def parse_date(raw):
    """
    Parse a raw date string into a consistent format, e.g. YYYY-MM-DD.
    Returns empty string if parsing fails.
    """
    try:
        dt = dateparser.parse(raw)
        return dt.strftime("%Y-%m-%d")
    except Exception as e:
        return raw.strip()

def clean_version(raw):
    """
    Clean up the version string, e.g. "VERSION v8.84" → "v8.84"
    """
    # find v or V followed by digits and dots
    m = re.search(r"v[0-9]+(?:\.[0-9]+)*", raw, re.IGNORECASE)
    if m:
        return m.group(0)
    # fallback
    return raw.strip()

def clean_filename(s):
    return re.sub(r"[^0-9a-zA-Z_]+", "_", s)

def scrape_dbf_news():
    url = "https://www.dbf2002.com/news.html"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Get all version headings (they are “### VERSION vX.YY (Date)” in markdown style)
        # On the HTML page, these appear as <h3> elements (or strong texts). Let’s inspect and adapt.
        elems = driver.find_elements(By.XPATH, "//h3[contains(., 'VERSION') or contains(translate(., 'version', 'VERSION'), 'VERSION')]")
        data = []
        for h3 in elems:
            raw = h3.text.strip()
            # Try split “VERSION v8.84 (October 2, 2025)” kind of string
            # Regex: VERSION <version> (<date>)
            m = re.match(r".*?VERSION\s+(.+?)\s*\((.+?)\)", raw, re.IGNORECASE)
            if m:
                ver_raw = m.group(1)
                date_raw = m.group(2)
            else:
                # fallback: maybe like "VERSION v8.84 October 2, 2025"
                parts = raw.split()
                # find the “v...” part
                ver_raw = ""
                for p in parts:
                    if re.match(r"v[0-9]+", p, re.IGNORECASE):
                        ver_raw = p
                        break
                # attempt last token(s) for date
                date_raw = parts[-2] + " " + parts[-1] if len(parts) >= 2 else ""
            
            version = clean_version(ver_raw)
            date_clean = parse_date(date_raw)

            # Also find a URL: sometimes the heading itself is not a link, but the section below may include a “Download / More info” link
            link = ""
            # Try to find an <a> following the heading
            try:
                a = h3.find_element(By.XPATH, "following-sibling::p//a")
                link = a.get_attribute("href")
            except:
                # fallback: search globally for link containing this version
                anchors = driver.find_elements(By.XPATH, f"//a[contains(text(), '{version}')]")
                if anchors:
                    link = anchors[0].get_attribute("href")

            data.append({
                "Version": version,
                "Date": date_clean,
                "URL": link
            })

        # Save to CSV
        if data:
            df = pd.DataFrame(data)
            fname = clean_filename("dbf2002") + ".csv"
            df.to_csv(fname, index=False, encoding="utf-8")
            print("Saved:", fname, " with", len(df), "rows.")
        else:
            print("No records found.")

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_dbf_news()
