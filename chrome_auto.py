import os
import time
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
MATCH = '[URGENT]: Confirm your Enrollment in NUST High Impact Training Program'

def login():
    driver.get("https://mail.google.com/mail/?ui=html")
    driver.maximize_window()
    load_dotenv()
    gmailId, passWord = os.getenv('GMAIL_ID'), os.getenv('GMAIL_PASSWORD')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(gmailId)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passWord)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    sleep(3)

def access_gmail():

    # driver.get('http://gmail.com')
    sleep(5)
    # Go thru messages list
    driver.find_element(By.PARTIAL_LINK_TEXT, MATCH).click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'Show').click()
    sleep(3)
    li = driver.find_elements(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table')
    for a in li:
        print(a.text)
        if "Mail Delivery Subsystem" not in a.text:
            a.click()
            sleep(3)
            driver.find_element(By.LINK_TEXT, 'Print').click()
            sleep(3)
            actions.send_keys(Keys.ENTER)
            break

    # take rest


if __name__ == '__main__':
    driver = webdriver.Chrome(options=chrome_options)
    actions = ActionChains(driver)
    login()
    access_gmail()
