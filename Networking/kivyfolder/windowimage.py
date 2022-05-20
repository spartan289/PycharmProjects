import ctypes
SPI_SETDESKWALLPAPER = 20
import requests
req = requests.get('https://forza-api.tk/')
import shutil
image = requests.get(req.json()['image'],stream=True)
print(image.status_code)
with open(r'C:\Users\sagar\PycharmProjects\Networking\kivyfolder\wallpaper.png','wb') as outfile:
    shutil.copyfileobj(image.raw,outfile)
del image
print(1)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\sagar\PycharmProjects\Networking\kivyfolder\wallpaper.png", 3)