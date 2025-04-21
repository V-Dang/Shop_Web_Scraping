from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re

# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set Selenium Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (without opening the browser)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
chrome_options.add_argument("--no-sandbox") # Only use if venv or Docker giving errors. Using this increases security risk
chrome_options.add_argument("--disable-dev-shm-usage") # Prevents memory issues
# chrome_options.add_argument("--enable-javascript")
# chrome_options.add_argument('--disable-notifications')

# Initialize and set up the Chrome WebDriver with selected configurations (options, service)
service = Service(ChromeDriverManager().install()) # Installs correct version of Chrome Driver depending on your version of Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
# driver.get("https://www.aritzia.com")
driver.get("https://www.aritzia.com/en/product/martine-poplin-midi-dress/109396.html?dwvar_109396_color=1274")

# Get page source after rendering and start parsing
html = driver.page_source
# print(html)
driver.quit()
# Search for item price
soup = BeautifulSoup(html, features="lxml")
print(soup.prettify)
# price = soup.findAll("span", attrs={"class":"{re.}"})
price = soup.find_all("p", attrs={"data-testid":"product-list-price-text"})
# print(soup)
# print(price)

# Close driver because CloudFlare detects BeautifulSoup 
# driver.quit()

# Using regex
# price = re.findall('"price":\d+[.]\d+', html)
# print(price)

# soup = BeautifulSoup(html, features="lxml")
# # Search for price of item


# price = soup.findAll("span", attrs={"class":"price-default"})
# # price = soup.find_all("div", attrs={"class":"product-price"})
# print(soup.text)
# # print(price)

#_____________________________________________________________________________

# # Print the page title
# page_title = driver.title
# print("Page Title:", page_title)

# # Example: Finding an element by tag name (e.g., h1 tag)
# heading = driver.find_element(By.TAG_NAME, 'h1').text
# print("Heading:", heading)

