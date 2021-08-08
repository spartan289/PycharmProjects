from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.microsoft.com/en-in/microsoft-teams/log-in')
sleep(2)
browser.find_element_by_xpath('//*[@id="office-Hero5050-zdjhwg8"]/section/div[1]/div[1]/div/div/div/div/div[1]/a').click()
sleep(2)
teams_mail = 'sagar205786@keshav.edu.du.ac.in'
browser.switch_to.window(browser.window_handles[1])
sleep(2)
browser.find_element_by_name("loginfmt").send_keys(teams_mail)
browser.find_element_by_id("idSIButton9").click()
sleep(2)
password  = 'Deepak40892'
browser.find_element_by_name("passwd").send_keys(password)
browser.find_element_by_id("idSIButton9").click()
sleep(2)
browser.find_element_by_id("idBtn_Back").click()

browser.find_element_by_class_name("app-bar-link app-bar-button ")