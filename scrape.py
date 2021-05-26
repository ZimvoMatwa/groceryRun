import requests
from bs4 import BeautifulSoup


heading = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


def checkers():
    cURL = "https://www.checkers.co.za/c-2614/All-Departments/Food/Bakery"
    page = requests.get(cURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    for ting in pot.findAll("a", {"class":"product-listening-click"}):
        print(ting.get_text().strip())

def picknPay():
    pURL = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Fresh-Food/Bakery/c/bakery703655157"
    page = requests.get(pURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    for ting in pot.findAll("div", {"class":"item-name"}):
        print(ting.get_text().strip())

def woolworths():
    wURL = "https://www.woolworths.co.za/cat/Food/Bread-Bakery-Desserts/_/N-1bm2new"
    page = requests.get(wURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    for ting in pot.findAll("a", {"class":"range--title"}):
        print(ting.get_text().strip())


def shoprite():
    sURL = "https://www.shoprite.co.za/c-2614/All-Departments/Food/Bakery"
    page = requests.get(sURL, headers=heading)
    pot = BeautifulSoup(page.content, "html.parser")

    for ting in pot.findAll("a", {"class":"product-listening-click"}):
        print(ting.get_text.strip())


# checkers()
# picknPay()
woolworths()
# shoprite()