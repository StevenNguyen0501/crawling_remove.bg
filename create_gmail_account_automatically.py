import os
import requests
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.request import urlretrieve as urldownload
from urllib.request import URLopener
import random


SYSTEM_OPERATION = 'Linux'
VERSION = '83'

# Stage 1
# # Add path to chrome driver version

column_name = ['First_name', 'Last_name', 'Primary_email', 'Secondary_email', 'Password', 'New_password']
file_csv = pd.read_csv('/media/tinvt/DATA2/crawling_rmbg/email_accounts.csv', names=column_name, header=None)
options = Options()
options.set_headless()

driver = webdriver.Chrome(
    executable_path=os.path.join(os.getcwd(), 'chrome_driver_{}'.format(SYSTEM_OPERATION),
                                 'version_{}'.format(VERSION),
                                 'chromedriver'))
opener = URLopener()
opener.addheader('User-Agent', 'whatever')

# Note that signed in quan2@dreamdesign.page
driver.get("https://admin.google.com/ac/home")
sleep(1)

# Fill email user name in text box
driver.find_element_by_name("identifier").send_keys("tinnvt@chayduocroi.page")

# Click button "Next"
driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(6)

# Fill password in text box
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("abcd1234")
#
driver.find_element_by_id('passwordNext').click()

driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[1]/div/div[2]/div/div/div/div[1]/span/div/div["
                             "3]/c-wiz/div/div/div[2]/a").click()

driver.implicitly_wait(3)

for index_line in range(len(file_csv['Primary_email'])):
    # print(file_csv['Primary_email'][index_line])
    # Click button "Add new user"

    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div["
                                 "1]/div[2]/div[1]/div/div[1]/div[1]/div/span/span").click()
    try:
        driver.find_element_by_xpath("//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/span/c-wiz/div[2]/div/div[1]/div/div["
                                 "1]/input").send_keys("{}".format(file_csv['First_name'][index_line]))
    except NoSuchElementException as Exception:
        print("Cant find this element, try to find id by another xpath!!!")
        driver.find_element_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/span/c-wiz/div[3]/div/div[1]/div/div["
            "1]/input").send_keys("{}".format(file_csv['First_name'][index_line]))
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/span/c-wiz/div[4]/div/div[1]/div/div["
                                 "1]/input").send_keys("{}".format(file_csv['Last_name'][index_line]))
    sleep(2)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/span/c-wiz/div[10]/c-wiz/div["
                                 "2]/div/div[1]/div/div[1]/input").send_keys("{}".format(file_csv['Password'][
                                                                                         index_line]))
    sleep(1)
    driver.implicitly_wait(1000)
    try:
        button = driver.find_element_by_xpath('/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[2]/span/span')
        sleep(1)
        button.click()
    except Exception as error:
        print(error)

    driver.implicitly_wait(19)

    try:
        driver.find_element_by_xpath('/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div[2]').click()
        sleep(2)
    except ElementClickInterceptedException as Exception:
        print(Exception)
    print("Added account {}".format(file_csv['First_name'][index_line]))

    driver.get('https://admin.google.com/ac/users')
    # driver.delete_all_cookies()
    sleep(random.randint(3, 6))
