import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from urllib.request import URLopener

SYSTEM_OPERATION = 'Linux'
VERSION = '83'

column_name = ['First_name', 'Last_name', 'Primary_email', 'Secondary_email', 'Password', 'New_password']
file_csv = pd.read_csv('/media/tinvt/DATA2/crawling_rmbg/email_accounts.csv', names=column_name, header=None)
options = Options()

driver = webdriver.Chrome(
    executable_path=os.path.join(os.getcwd(), 'chrome_driver_{}'.format(SYSTEM_OPERATION),
                                 'version_{}'.format(VERSION),
                                 'chromedriver'))
opener = URLopener()
opener.addheader('User-Agent', 'whatever')

driver.get("https://accounts.google.com/")
sleep(1)

for index, index_line in enumerate(range(len(file_csv['Primary_email']))):
    print(file_csv['Primary_email'][index_line])

    # Fill in box "Email or phone"
    driver.find_element_by_id("identifierId").send_keys("{}".format(file_csv['Primary_email'][index_line] + '@chayduocroi.page'))
    # Click button "Next"
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    driver.implicitly_wait(1000)
    # Fill "Enter your password" //*[@id="password"]/div[1]/div/div[1]/input
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("{}".format(file_csv['Password'][index_line]))
    # Click button "Next"
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()
    sleep(3)
    driver.implicitly_wait(1000)

    # Click "Accept"
    driver.find_element_by_xpath("//*[@id='accept']").click()
    sleep(2)

    # Fill "Create password"
    driver.find_element_by_xpath("//*[@id='Password']").send_keys("{}".format(file_csv['New_password'][index_line]))
    driver.implicitly_wait(1000)
    driver.find_element_by_xpath("//*[@id='ConfirmPassword']").send_keys("{}".format(file_csv['New_password'][index_line]))
    sleep(2)

    # Click "Change password"
    driver.find_element_by_xpath("//*[@id='submit']").click()
    sleep(2)

    # Sign out
    driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div/div/a/img").click()
    driver.find_element_by_xpath("//*[@id='gb_71']").click()
    driver.implicitly_wait(1000)

    # Click "Delete account"
    driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[3]/div/div/div[2]").click()
    driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/ul/li[1]/div").click()
    # /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/ul/li[1]/div
    # //*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/ul/li[1]/div
    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[3]/div[1]/span/span").click()
    # /html/body/div[5]/div/div[2]/div[3]/div[1]/span/span
    sleep(3)

    driver.get("https://accounts.google.com/")

