from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Selenium Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening the browser)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
chrome_options.add_argument("--no-sandbox") # Only use if venv or Docker giving errors. Using this increases security risk
chrome_options.add_argument("--disable-dev-shm-usage") # Prevents memory issues
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument('--disable-notifications')

# Initialize and set up the Chrome WebDriver with selected configurations (options, service)
service = Service(ChromeDriverManager().install()) # Installs correct version of Chrome Driver depending on your version of Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("https://prixworkshop.com/products/friendship-bikini-snow?variant=46299537703126")
driver.implicitly_wait(5)

# Get page source after rendering and start parsing
html = driver.page_source
# print(html)

# Search for item info
soup = BeautifulSoup(html, features="lxml")
# print(soup.prettify)
x = soup.find("div", attrs={"class":"product-info"})
item_name = x.find("h1", attrs={"class":"product-single__title"}).text.strip()
item_price_regular = x.find("div", attrs={"class":"price__regular"}).text.strip()
item_price_sale = x.find("div", attrs={"class":"price__sale"}).text.strip()

# print(x)
print(item_name)
print(item_price_regular)

driver.quit()
