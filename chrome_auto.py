import os
import time
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver.get("https://mail.google.com/mail/u/0/#inbox")
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

def gettomail():
    # find all elements with class name '[URGENT]: Confirm your Enrollment in NUST High Impact Training Program'
    driver.find_element(By.XPATH, "//*")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login()
    gettomail()
    driver.close()
