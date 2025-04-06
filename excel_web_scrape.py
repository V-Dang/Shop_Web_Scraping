from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def get_price(url_link):
    chrome_options = Options()                 # Set Selenium Chrome options
    chrome_options.add_argument("--headless")  # Run in headless mode (without opening the browser)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
    chrome_options.add_argument("--no-sandbox") # Only use if venv or Docker giving errors. Using this increases security risk
    chrome_options.add_argument("--disable-dev-shm-usage") # Prevents memory issues
    chrome_options.add_argument("--enable-javascript")
    chrome_options.add_argument('--disable-notifications')

    # Initialize and set up the Chrome WebDriver with selected configurations (options, service)
    service = Service(ChromeDriverManager().install()) # Installs correct version of Chrome Driver depending on your version of Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url_link)                        # Open the website
    driver.implicitly_wait(5)

    html = driver.page_source                   # Get page source after rendering and start parsing
    # print(html)

    driver.quit()

    # Search for item info
    soup = BeautifulSoup(html, features="lxml")
    # print(soup.prettify)
    x = soup.find("div", attrs={"class":"product-info"})
    item_name = (x.find("h1", attrs={"class":"product-single__title"})).text.strip()
    item_price_regular = (x.find("div", attrs={"class":"price__regular"})).text.strip()
    # item_price_sale = x.find("div", attrs={"class":"price__sale"}).text.strip()

    # print(x)
    return url_link, item_name, item_price_regular, # item_price_sale

def update_excel():
    df = pd.read_excel("clothing_links.xlsx")
    row_list = []

    for index, row in df.iterrows():                    # Scrape links for prices and add to list
        item = get_price(row["link"])
        row_list.append(item)
        print(f"Updating {item[1]} price.")

    df1 = pd.DataFrame(row_list, columns=["url_link", "item_name", "item_price_regular"])           # Convert list to df

    with pd.ExcelWriter('clothing_links.xlsx') as writer: 
        df.to_excel(writer, sheet_name="prixworkshop")                               # Write to excel
        df1.to_excel(writer, sheet_name="prixworkshop_prices") 

update_excel()