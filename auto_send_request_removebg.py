import os
import requests
import csv
import pandas as pd
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
from urllib.request import urlretrieve as urldownload
from urllib.request import URLopener
import config as cfg

column_name = ['First_name', 'Last_name', 'Primary_email', 'Secondary_email', 'Password', 'New_password']
file_csv = pd.read_csv('/media/tinvt/DATA2/crawling_rmbg/email_accounts.csv', names=column_name, header=None)

driver = webdriver.Chrome(
    executable_path=os.path.join(os.getcwd(), 'chrome_driver_{}'.format(cfg.SYSTEM_OPERATION),
                                 'version_{}'.format(cfg.VERSION),
                                 'chromedriver'))
opener = URLopener()
opener.addheader('User-Agent', 'whatever')


for index_line in range(len(file_csv['Primary_email'])):
    # # Round 1:
    # print(file_csv['Primary_email'][index_line])
    # # # Sign in Gmail account
    # # Fill in box "Email or phone"
    #
    # driver.get("https://accounts.kaleido.ai/users/sign_up")
    # # Fill email user name in text box
    # # //*[@id="user_email"]
    # driver.find_element_by_xpath("//*[@id='user_email']").send_keys(
    #     "{}".format(file_csv['Primary_email'][index_line] + '@chayduocroi.page'))
    # sleep(random.randint(1, 2))
    #
    # # Fill password
    # # //*[@id="user_password"]
    # driver.find_element_by_xpath("//*[@id='user_password']").send_keys(
    #     "{}".format(file_csv['New_password'][index_line]))
    # sleep(random.randint(1, 2))
    #
    # # Fill confirm password
    # # //*[@id="user_password_confirmation"]
    # driver.find_element_by_xpath("//*[@id='user_password_confirmation']").send_keys(
    #     "{}".format(file_csv['New_password'][index_line]))
    # sleep(random.randint(1, 2))
    #
    # # Click tick "I agree"
    # # //*[@id="user_terms_of_service"]
    # driver.find_element_by_xpath("//*[@id='user_terms_of_service']").click()
    # sleep(random.randint(1, 2))
    #
    # # Click tick "Notify me"
    # # /html/body/main/div[2]/div[1]/div/form/div[6]/label/input[2]
    # driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div/form/div[6]/label/input[2]").click()
    # sleep(random.randint(1, 2))
    #
    # # Click button "Sign up"
    # # //*[@id="new_user"]/div[8]/button
    # driver.find_element_by_xpath("//*[@id='new_user']/div[8]/button").click()
    # sleep(90)
    #
    # # ----------------------------------------------------------------------------------------------#
    # driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    # sleep(random.randint(1, 2))
    # driver.find_element_by_id("identifierId").send_keys(
    #         "{}".format(file_csv['Primary_email'][index_line] + '@chayduocroi.page'))
    # sleep(random.randint(1, 2))
    # # Click button "Next"
    # driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    # driver.implicitly_wait(1000)
    # sleep(random.randint(1, 2))
    # # Fill "Enter your password" //*[@id="password"]/div[1]/div/div[1]/input
    # driver.find_element_by_xpath(
    #     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div["
    #     "1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(
    #     "{}".format(file_csv['New_password'][index_line]))
    # # Click button "Next"
    # driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()
    # sleep(random.randint(1, 3))
    # driver.implicitly_wait(1000)
    # # Got it /html/body/div[25]/div[2]    /html/body/div[25]/div[2]
    # driver.find_element_by_xpath("/html/body/div[23]/div[1]/div/div[2]/div[2]").click()
    # sleep(random.randint(1, 3))
    # # Select first email //*[@id=":20"]     /html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/table/tbody/tr[1]
    # # driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[4]/div[2]/div/table/tbody/tr[1]").click()
    # # Activate account /html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":5y"]/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":5w"]/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":2k"]/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":2k"]/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":2k"]/div[1]/div[1]/div[2]/p[3]/a
    # # /html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[2]/p[3]/a
    # # //*[@id=":2k"]/div[1]/div[1]/div[2]/p[3]/a
    # # /html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[2]/p[3]/a
    # # sleep(6)
    # driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div["
    #                              "1]/div/div/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div["
    #                              "1]/div[2]/div[3]/div[3]/div/div[1]/div[1]/div[2]/p[3]/a").click()
    # driver.get(driver.current_url)
    # sleep(6)
    # # Home page /html/body/nav/a/img
    # driver.find_element_by_xpath("/html/body/nav/a/img").click()
    # sleep(random.randint(1, 3))
    # # # Click button Login/Sign in /html/body/nav/div/div/div[2]/a      //*[@id="navbar-user-options"]/a
    # # driver.find_element_by_xpath("//*[@id='navbar-user-options']/a").click()
    # # sleep(2)
    # # Click "API Documentation"
    # driver.find_element_by_xpath("/html/body/footer/div[1]/div/div[1]/div[2]/div[1]/a").click()
    # sleep(random.randint(1, 3))
    # # Click Get API Key
    # driver.find_element_by_class_name("btn btn-primary btn-lg").click()
    # sleep(random.randint(1, 3))
    # # Click "Show"
    # driver.find_elements_by_class_name("btn btn-outline-primary toggle-api-key-btn").click()
    # sleep(random.randint(1, 3))
    # # Copy "API key"
    # api_key = driver.find_element_by_class_name("api-key").text()
    # sleep(random.randint(1, 3))
    # print('API Key: ', api_key)
    # text_file = open('/media/tinvt/DATA2/crawling_rmbg/api_key.txt', 'w+')
    # text_file.write(api_key, "\n")
    # sleep(6)

    # --------------------------------------------------------------------------------#

    # # Round 2
    driver.get("https://accounts.kaleido.ai/users/sign_in")
    # Fill email user name in text box
    # //*[@id="user_email"]
    driver.find_element_by_xpath("//*[@id='user_email']").send_keys(
        "{}".format(file_csv['Primary_email'][index_line] + '@chayduocroi.page'))
    sleep(random.randint(1, 2))

    # Fill password
    # //*[@id="user_password"]
    driver.find_element_by_xpath("//*[@id='user_password']").send_keys(
        "{}".format(file_csv['New_password'][index_line]))
    sleep(random.randint(1, 2))

    # Click button "Log in"
    driver.find_element_by_xpath("//*[@id='new_user']/div[4]/div[2]/button").click()

    # Across captcha
    sleep(90)

    # Click logo Remove BG
    driver.find_element_by_xpath("/html/body/nav/a/img").click()

    sleep(2)
    # Click "API Documentation"
    driver.find_element_by_xpath("/html/body/footer/div[1]/div/div[1]/div[2]/div[1]/a").click()
    sleep(random.randint(1, 3))
    # Click Get API Key
    driver.find_element_by_xpath("//*[@id='page-content']/div[1]/div/div/div/p[3]/a").click()
    sleep(random.randint(1, 3))
    # Click "Show"
    driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[2]/p/a").click()
    sleep(random.randint(1, 3))
    # Copy "API key"
    api_key = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[2]/p/span/code").text
    print('api_key', api_key)
    sleep(random.randint(1, 3))
    print('API Key: ', api_key)
    with open('/media/tinvt/DATA2/crawling_rmbg/api_key.txt', 'w+') as text_file:
        text_file.write("%d \n" %str(api_key))
        text_file.close()
    sleep(3)
    driver.close()
