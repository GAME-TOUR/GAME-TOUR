from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import datetime
import time

def scrap_gameList(driver): 
    gameLi = list()
  
    # 스팀 게임 목록 
    driver.get("https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1")

    gameRows = driver.find_element(By.ID, 'search_resultsRows')
    games = gameRows.find_elements(By.TAG_NAME, 'a')
    
    print(type(gameRows))
    print(type(games))
    

driver = webdriver.Chrome()
scrap_gameList(driver)
