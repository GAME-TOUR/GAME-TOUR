from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import datetime
import time

def xbox_login(driver):
    xbox_account = ''
    xbox_password = ''
    
    def login_action():
        account = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        account.click()
        account.send_keys(xbox_account)
        account.send_keys(Keys.ENTER)

        time.sleep(3)
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password.click()
        password.send_keys(xbox_password)
        password.send_keys(Keys.ENTER)
        
        
        time.sleep(3)
        driver.get("https://www.xbox.com/ko-kr/games/all-games?cat=upcoming")
        #loginState = driver.find_element(By.CSS_SELECTOR, "input[id='idBtn_Back']")
        #loginState.click()
        

    driver.get("https://www.xbox.com/ko-kr/games/all-games?cat=upcoming")
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, 'mectrl_topHeader').click()
    
    driver.implicitly_wait(10)
    
    try:
        login_action()
        time.sleep(5)
    except:
        driver.find_element(By.CLASS_NAME, 'mectrl_topHeader').click()
        time.sleep(5)
        login_action()
        
        
    driver.implicitly_wait(10)
    

  