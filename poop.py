import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as pp

from time import sleep
from random import randint

heading = {"Accept-Language": "en-US, en;q=0.5"}
pages = pp.arange(1, 1001, 60)

# DATA STORAGE
item_name = []
item_price = []
item_quantity = []
special_price = []
total_cost = 0

# OUR STORE LIST
# def woolworths():
for page in pages:
    wURL = "https://www.woolworths.co.za/cat/Food/Fruit-Vegetables-Salads/_/N-lllnam?No=" + str(pages) + "&Nrpp=60"
    page = requests.get(wURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")
    details = pot.findAll("div", {"class": "product-list__item"})
    sleep(randint(2, 10))

    for cont in details:
        item = cont.find("a", class_="range--title").get_text().strip()
        item_name.append(item)
        price = cont.find("strong", class_="price").get_text().strip()
        item_price.append(price)
        special = cont.find("div", class_="product__special").get_text().strip() \
            if cont.find("div", class_="product__special").get_text().strip() else '-'
        special_price.append(special)


# pandas skelly
groceryList = pd.DataFrame({
    "Item": item_name,
    # "Quantity": item_quantity,
    "Price": item_price,
    "Special Price": special_price
})

# convert our price from string to int so we can do big brain math with it
groceryList["Price"] = groceryList["Price"].map(lambda x: x.lstrip("R"))
# groceryList["Price"] = groceryList["Price"].str.extract('(\d+)')
groceryList["Price"] = pd.to_numeric(groceryList["Price"], errors="coerce")
total_cost = sum(groceryList["Price"])

# checkers()
# picknPay()
# woolworths()
# shoprite()
print(groceryList)
print(round(groceryList["Price"], 2))
# groceryList.to_csv("groceries.csv")
