import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as pp

from time import sleep
from random import randint

heading = {"Accept-Language": "en-US, en;q=0.5"}
pages = pp.arange(0, 7,1 )


# DATA STORAGE
item_name = []
item_price = []
item_quantity = []


# OUR STORE LIST
def checkers():
    # for page in pages:
    cURL = "https://www.checkers.co.za/c-2614/All-Departments/Food/Bakery?q=%3Arelevance%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff&page=3" # + str(pages)
    page = requests.get(cURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    for ting in pot.findAll("div", {"class": "item-product"}):
        item = ting.find("a", class_="product-listening-click").get_text().strip()
        item_name.append(item)
        price = ting.find("span", class_="now").get_text().strip()
        item_price.append(price)
        # return item_price, item_name


def picknPay():
    for page in pages:
        pURL = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Fresh-Food/Bakery/c/bakery703655157"
        page = requests.get(pURL, headers=heading)
        pot = BeautifulSoup(page.content, "html.parser")
        # sleep(randint(2, 5))

        for ting in pot.findAll("div", {"class": "productCarouselItemContainer"}):
            item = ting.find("div", class_="item-name").get_text().strip()
            item_name.append(item)
            price = ting.find("div", class_="currentPrice").get_text().strip()
            item_price.append(price)
            # return item_price, item_name


def woolworths():
    wURL = "https://www.woolworths.co.za/cat/Food/Bread-Bakery-Desserts/_/N-1bm2new"
    page = requests.get(wURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    details = pot.findAll("div", {"class": "product-list__item"})
    for cont in details:
        item = cont.find("a", class_="range--title").get_text().strip()
        item_name.append(item)
        price = cont.find("strong", class_="price").get_text().strip()
        item_price.append(price)
        # return item_price, item_name


# def shoprite():
sURL = "https://www.shoprite.co.za/c-2614/All-Departments/Food/Bakery"
page = requests.get(sURL, headers=heading)
pot = BeautifulSoup(page.content, "html.parser")

for ting in pot.findAll("div", {"class": "product-item"}):
    dos = ting.find("a", class_="product-listening-click").get_text().strip()
    item_name.append(dos)
    print(dos)
    uno = ting.find("span", class_="now").get_text().strip()
    item_price.append(uno)
    print(uno)
    # return item_price, item_name
    # for ting in pot.findAll("a", {"class": "product-listening-click"}):
    #     print(ting.get_text.strip())


# pandas skelly
groceryList = pd.DataFrame({
    "Item": item_name,
    # "Quantity": item_quantity,
    "Price": item_price
})

# cleaning
# groceryList["Price"] = groceryList["Price"].map(lambda x: x.lstrip('R ')).str.extract(r'(\d+)', '.').astype(float)


# checkers()
# picknPay()
# woolworths()
# shoprite()
# print(groceryList)
# groceryList.to_csv("groceries.csv")

# FUTURE FEATURES---\
#have each store create it's own sheet (xlsx, not csv)
# REPLACE PRE-DEFINED STORES WITH A WEB SEARCH FROM INPUT
# USER ENTERS THEIR BUDGET + LIST, SCRIPT RETURNS LIST AND A CALCULATION OF COST
# SEPARATE QUANTITY AND MAKE IT USER SPECIFIC
# USE USER LOCATION FOR STORES NEARBY
# WEB-BASED: USER CAN VIEW RESULTS IN THE WEB OR DOWNLOAD THE CSV