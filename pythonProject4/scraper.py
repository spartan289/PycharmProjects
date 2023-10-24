import requests
URL = 'https://www.amazon.in/Snapdragon-Resolution-Refresh-Display-Storage/dp/B09XXWK46R?ref_=Oct_DLandingS_D_83d3b03d_62&th=1' \

# //*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
r = requests.get(URL,headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

price = soup.find('span', attrs={'class':'a-price-whole'})
print(price)