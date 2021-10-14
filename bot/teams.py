import datetime
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import utils

df = pd.read_excel(r'C:\Users\sagar\PycharmProjects\bot\timetable.xlsx')


def openbrowser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2,
             "profile.default_content_setting_values.media_stream_camera": 1,
             "profile.default_content_setting_values.media_stream_mic": 1,

             }
    chrome_options.add_experimental_option("prefs", prefs)
    path = r"C:\Users\sagar\PycharmProjects\bot\chromedriver.exe"
    return webdriver.Chrome(executable_path=path ,options=chrome_options)


browser = openbrowser()


def login():
    browser.get(
        'https://go.microsoft.com/fwlink/p/?LinkID=873020&clcid=0x4009&culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn')
    time.sleep(2)
    time.sleep(2)
    teams_mail = 'sagar205786@keshav.edu.du.ac.in'
    time.sleep(2)
    time.sleep(2)
    browser.find_element_by_name("loginfmt").send_keys(teams_mail)
    browser.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    password = 'Deepak40892'
    browser.find_element_by_name("passwd").send_keys(password)
    browser.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    browser.find_element_by_id("idBtn_Back").click()


def startmeet(link):
    browser.get(link)
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="buttonsbox"]/button[2]').click()
    time.sleep(10)
    option = Options()
    option.add_argument("--disable-infobars")

    time.sleep(5)
    browser.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()
    browser.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]').click()
    browser.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()


def endmeet():
    browser.find_element_by_xpath('//*[@id="hangup-button"]').click()


current_time = datetime.datetime.now()
day = current_time.strftime("%A")
login()
time.sleep(10)
for i in range(23):
    if df.loc[i][3] == day:

        current_second = utils.convertseconds(current_time)
        start_second = utils.convertseconds(df.loc[i][1])
        end_second = utils.convertseconds(df.loc[i][2])
        if current_second > end_second:
            continue
        if current_second >= start_second:
            if start_second <= current_second <= end_second:
                startmeet(df.loc[i][4])
            time.sleep(end_second - current_second + 30)
            endmeet()
        else:
            print("Currently no class is now")
            time.sleep(start_second - current_second + 30)
            current_second = utils.convertseconds(current_time)
            if current_second >= start_second:
                if start_second <= current_second <= end_second:
                    startmeet(df.loc[i][4])
                time.sleep(end_second - current_second)
                endmeet()
