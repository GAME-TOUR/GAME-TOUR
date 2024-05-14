from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from nintendo_gameListCrawling import scrap_gameList, popup_close

opt = Options()
# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 
# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)

pageList = list()

# for i in range(1, 94): 
#   print(f'page{i} crawling')
#   url = f'https://store.nintendo.co.kr/all-released-games?p={i}&product_list_limit=48'
#   driver.get(url)
#   if i == 1: 
#     popup_close(driver)
#     
#   pageList.append(scrap_gameList(driver))
  
driver.get("https://store.nintendo.co.kr/all-released-games?p=1&product_list_limit=48")
popup_close(driver)
test = scrap_gameList(driver)
print(test)