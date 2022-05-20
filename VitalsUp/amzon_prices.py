import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
page = requests.get(
    'https://www.amazon.in/s?i=electronics&bbn=976419031&rh=n%3A976419031%2Cp_85%3A10440599031%2Cp_89%3ANoise&pf_rd_i'
    '=976419031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=c0947463-d292-462d-96bf-f66554f76419&pf_rd_r=S2RY52H8QPBKD8PCFV6J'
    '&pf_rd_s=merchandised-search-7&ref=AF_WIN_bub_w_cml_t_3',
    headers=HEADERS)

soup = BeautifulSoup(page.content, features="lxml")
result_price = []
result_name = []

items = []
# import matplotlib
# import numpy as np
for item in soup.find_all("div", {"data-component-type": "s-search-result"}):
    if item.find("span", {"class": 'a-size-base a-color-base a-text-normal'}) != None:
        result_name.append(item.find("span", {"class": 'a-size-base a-color-base a-text-normal'}).text)
    elif item.find("span", {"class": 'a-size-medium a-color-base a-text-normal'}) != None:
        result_name.append(item.find("span", {"class": 'a-size-medium a-color-base a-text-normal'}).text)
    try:
        result_price.append(item.find("span", {"class": 'a-price-whole'}).text)
    except:
        print("Price not found ")
        result_price.append(0)

result = zip(result_name, result_price)
for i in result:
    print(i)
print(len(result_name))
# data-component-type="s-search-result"
