from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import datetime
import time

from nintendo_gameListCrawling import scrap_gameList, popup_close
from nintendo_gameInfoCrawling import gameinfo_scrap
from nintendo_concat           import nintendo_concat

opt = Options()
# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 
# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)

gameList = list()
detailList = list()

for i in range(1, 2): 
  print(f'page{i} crawling')
  url = f'https://store.nintendo.co.kr/all-released-games?p={i}&product_list_limit=48'
  driver.get(url)
  if i == 1: 
    popup_close(driver)
    
  gameList = scrap_gameList(driver)
  print("gameList scrapped successfully")
  
for i in range(len(gameList)):
  print(f"{i} title: {gameList[i]['title']}")
  detail = gameinfo_scrap(driver, gameList[i]['url'])
  detailList.append(detail)

nintendo_concat(gameList, detailList, "nintendo")