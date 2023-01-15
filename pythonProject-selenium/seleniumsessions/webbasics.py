from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\sagar\\OneDrive\\Documents\\Driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME,'q').send_keys("labs")
option_list=
time.sleep(10)
driver.quit()