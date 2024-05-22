from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pandas as pd
import datetime
import time

FILTERWORDS = [
    '디럭스','Deluxe',
    '프리미엄','Premium',
    '얼티밋','Ultimate',
    '얼티메이트',
    '컴플리트', 'Complete',
    '디피니티브', 'Definitive',
    '다운로드', 'Download',
    '스페셜', 'Special',
    '번들', 'Bundle',
    '애드온', 'Add-On'
    
    ]

def scrap_gamelist(driver):
  gameList = list()
  
  WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='gameDivLink']")))
  print('Loading Done, Scrap start')
  
  games = driver.find_elements(By.XPATH, "//*[@id='ContentBlockList_1']/div[1]/div[2]/div[5]")
  print(len(games))
  
  for game in games:
      filterCheck = False
      
      title = game.find_element(By.CSS_SELECTOR, "h3[itemprop='product name']").text
      url = game.find_element(By.TAG_NAME, 'a').get_attribute('href')              
      releaseDate = game.get_attribute('data-releasedate')
      releaseDate = releaseDate[:10]
      
      for word in FILTERWORDS:
          if word in title:
              filterCheck = True
               
      if filterCheck == True:
          continue
          
      pageGame = {
          'title': title,
          'url': url,
          'date': releaseDate
      }
      
      gameList.append(pageGame)
  
  print(gameList)
  return gameList
  
  
  