from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com/')
sleep(2)
browser.find_element_by_class_name("KPnG0").click()
sleep(2)
fb_name = "9310399182"
fb_pass = "Jyoti9398"
browser.find_element_by_name("email").send_keys(fb_name)
browser.find_element_by_name("pass").send_keys(fb_pass)
browser.find_element_by_id('loginbutton').click()

