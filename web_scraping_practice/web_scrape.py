from bs4 import BeautifulSoup
import requests

# aritzia_page = requests.get("https://www.aritzia.com/en/product/martine-poplin-midi-dress/109396.html?dwvar_109396_color=1274")
# soup = BeautifulSoup(aritzia_page.text, "html.parser")
# price = soup.find_all("div", attrs={"class":"product-price"})
# print(price)

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
authors = soup.find_all("small", attrs={"class":"author"})
div = soup.find_all("div", attrs={"class":"quote"})
print(div)
for author in authors:
    print(author.text)
# print(soup)