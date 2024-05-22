from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import datetime
import time

from xbox_gameList import scrap_gamelist
from xbox_gameInfo import scrap_gameinfo
from xbox_concat   import xbox_concat 

opt = Options()
# 엑스박스 상점 페이지 주소
url = 'https://www.xbox.com/ko-kr/games/all-games?cat=all#'

# 브라우저 꺼짐 방지 옵션 - 개발용
opt.add_experimental_option("detach", True) 
# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

gameList = list()
detailList = list()

driver.get(url)
driver.implicitly_wait(2)
  
driver.find_element(By.XPATH, "//*[@id='ContentBlockList_1']/div[1]/div[1]/div[2]/span[1]/a[1]").click()
driver.implicitly_wait(10)
print("Page Refreshed")

gameList = scrap_gamelist(driver)

for i in range(len(gameList)):
  kor = gameList[i]['url']
  eng = gameList[i]['url'].replace('ko-kr', 'en-us')
  
  detail = scrap_gameinfo(driver, driver_eng, kor, eng) 
  detailList.append(detail) 

xbox_concat(gameList, detailList, 'xbox')



# xbox_login(driver)

# pageList = driver.find_element(By.CSS_SELECTOR, "button[id='unique-id-for-paglist-generated-select-menu-trigger']")
# pageList.click()
# time.sleep(0.5)
# menu = driver.find_element(By.CSS_SELECTOR, "li[id='unique-id-for-paglist-generated-select-menu-3']")
# menu.click()
# print("Xbox Login Complete")