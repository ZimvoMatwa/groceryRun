import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Fresh-Food/Bakery/c/bakery703655157"

headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("thehuman.zimvo@gmail.com", "hbzipuatxfqocdnf")

    subject = "backed goods"
    body = "before you waste your money, here is the grocery list"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "thehuman.zimvo@gmail.com",
        "zimvo09@outlook.com",
        msg
    )
    print("Email sent")

    server.quit()

def checkPrice():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    # for eachItem in soup.findAll("div", "item-name"):
    #     print(eachItem.get_text().strip()) #get_text() removes the html tags, .strip() removes white space

    title = soup.find("div", {"class":"item-name"}).get_text().strip()
    price = soup.find("div", {"class":"currentPrice"}).get_text().strip()
    intPrice = float(price[1:6])

    # if intPrice <= 3999.0:
    #     send_mail()

# while True:
#     checkPrice()
#     time.sleep(60*60*5)