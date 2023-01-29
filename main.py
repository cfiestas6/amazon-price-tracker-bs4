from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.es/Dell-Port%C3%A1til-pulgadas-procesador-i7-1165G7/dp/B09BK2RQGT/ref=sr_1_13?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3AXYJOQ388SQG&keywords=xps+13&qid=1675005957&sprefix=xps+13%2Caps%2C98&sr=8-13"

response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7"
})

web = response.text
soup = BeautifulSoup(web, "lxml")

price_tag = soup.find(name="span", class_="a-price-whole")
cents_tag = soup.find(name="span", class_="a-price-fraction")
price_str_raw = price_tag.get_text() + cents_tag.get_text()
price_str = price_str_raw.replace(".", "").replace(",", ".")
price = float(price_str)
if price < 1100:
    message = f"The product is now at: {price}"
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
                from_addr=YOUR_EMAIL,
                to_addrs=YOUR_EMAIL,
                msg=f"Subject:Amazon Price Alert!"
        )
