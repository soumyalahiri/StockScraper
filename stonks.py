import requests
import time
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import string

# Variable declarations
#symbols = ["aapl", "goog", "msft", "yhoo", "amzn", "fb", "twtr", "nflx"]
#numCompanies = len(symbols)
#values = []
#arrows = []

url = "https://markets.businessinsider.com/stocks/goog-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[133:141]
print("GOOG: $" + price)

url = "https://markets.businessinsider.com/stocks/amzn-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[133:141]
print("AMZN: $" + price)

url = "https://markets.businessinsider.com/stocks/aapl-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[132:138]
print("AAPL: $" + price)

url = "https://markets.businessinsider.com/stocks/fb-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[132:138]
print("FB: $" + price)

url = "https://markets.businessinsider.com/stocks/nflx-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[132:138]
print("NFLX: $" + price)

url = "https://markets.businessinsider.com/stocks/spot-stock"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
price_raw = soup.find("span", {"class": "push-data aktien-big-font text-nowrap"})
i = 0
price = str(price_raw)
price = price[132:138]
print("SPOT: $" + price)