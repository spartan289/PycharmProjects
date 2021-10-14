from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import datetime
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def login():
    browser.get('https://go.microsoft.com/fwlink/p/?LinkID=873020&clcid=0x4009&culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn')
    time.sleep(2)
    teams_mail = 'sagar205786@keshav.edu.du.ac.in'
    time.sleep(2)
    time.sleep(2)
    browser.find_element_by_name("loginfmt").send_keys(teams_mail)
    browser.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    password  = 'Deepak40892'
    browser.find_element_by_name("passwd").send_keys(password)
    browser.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    browser.find_element_by_id("idBtn_Back").click()
def openbrowser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2,
             "profile.default_content_setting_values.media_stream_camera":1,
             "profile.default_content_setting_values.media_stream_mic": 1,

             }
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options)

browser = openbrowser()
login()
time.sleep(10)
browser.get('https://teams.microsoft.com/l/meetup-join/19%3ayukX1AtG2fcrdorOinTcnDFXQcZVMaGsD7WlKVKwlBw1%40thread.tacv2/1626686553406?context=%7b%22Tid%22%3a%2234c8cd12-1b99-48f3-83f7-df418b097cde%22%2c%22Oid%22%3a%22f9413fc1-194f-49dd-9623-fdbe73bd9c4b%22%7d')
time.sleep(4)
browser.find_element_by_xpath('//*[@id="buttonsbox"]/button[2]').click()
time.sleep(10)
option = Options()
option.add_argument("--disable-infobars")

time.sleep(5)
browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()
browser.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
browser .find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()
