# Web Scraping

---

## What is Web Scraping?

- **Definition:**  
  Web scraping is an **automatic method** to obtain large amounts of data from websites.

- **Purpose:**  
  Converts **unstructured HTML** or other web data into **structured formats** like CSV, JSON, or databases.

- **Example:**  
  Websites like **Amazon** or **Flipkart** contain massive product data.  
  If we want to extract that data automatically — we use **web scraping**.

---

## Key Points

- Web Scraping can be performed using **Python libraries** such as:

  - `BeautifulSoup`
  - `Selenium`
  - Frameworks such as **Scrapy**

- The extracted data can be used for:

  - **Analysis**
  - **Predictions**
  - **Reposting** or **republishing** on other websites

- **Applications:**
  - Price Monitoring
  - Market Research
  - News Monitoring
  - Sentiment Analysis
  - Email Marketing

---

## Why Scraping?

- Companies can scrape **their own** and **competitors’** product data to:

  - Analyze how pricing strategies affect sales
  - Adjust prices to optimal levels

- Helps in:

  - **Analyzing consumer trends**
  - **Understanding future directions** for the company

- Can extract various metadata such as:
  - Version numbers
  - End-of-life (EOL) dates
  - Year of release
  - Names
  - IP addresses
  - Hostnames

---

## Selenium Overview

- **Definition:**  
  Selenium is a **powerful tool** for controlling web browsers through code and performing **browser automation**.

- **Features:**

  - Works on all major **browsers** (Chrome, Firefox, Edge, etc.)
  - Runs on all **operating systems**
  - Scripts can be written in various languages (Python, Java, etc.)
  - Compatible with multiple platforms and browsers

- **Key Component:**  
  **WebDriver** — acts as an **API module** containing classes, functions, and methods to automate browser tasks.

---

---

## Selenium WebDriver Features

### Key Advantages of Selenium WebDriver

1. **Multi-Browser Compatibility**
2. **Multiple Language Support**
3. **Speed & Performance**
4. **Community Support**
5. **Open Source & Portable**
6. **Works on Different Operating Systems**
7. **Add-ons & Reusability**
8. **Simple Commands**
9. **Reduced Test Execution Time**
10. **No Server Installation Required**

---

## Selenium Architecture

### 1. Selenium Client Library

- Selenium developers provide language-specific libraries (Python, Java, etc.) to interact with the WebDriver.

### 2. JSON Wire Protocol

- Acts as an **intermediate** between client and server.
- Converts requests and responses:
  - Client → JSON → Server (Browser)
  - Server → JSON → Client
- Enables structured communication between Selenium and browser drivers.

### 3. Browser Driver

- Establishes a **secure connection** with the browser.
- Executes the commands received from Selenium without exposing browser internals.

---

---

## Installation and Drivers

- **Install Selenium:**
  ```bash
  pip install selenium
  ```
- Selenium requires a driver to interface with the chosen browser.
- Different types of drivers available in Selenium WebDriver are:
  1. ChromeDriver
  2. FirefoxDriver
  3. InternetExplorerDriver
  4. EdgeDriver
  5. RemoteWebDriver

---

## Key points

- Install a WebDriver compatible with your Chrome version.
- Import libraries `Service`, `By`, and `ChromeDriverManager` from Selenium.
- Create driver by providing the appropriate browser path.
- Open the website using:
  ```python
  driver.get("url")
  ```
- Identify the tags and find elements by specifying their **XPATH**.
- **XPATH** contains the path of the element located on the web page.
  **Syntax:**

```xpath
//tag_name[@attribute='value']
```
