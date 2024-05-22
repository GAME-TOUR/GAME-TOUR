from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

from playstation_GameListCrawling import page_scrap
from playstation_GameInfoCrawling import scrap_detail
from playstation_concat           import playstation_concat

opt = Options()
# 플레이스테이션 상점 페이지 주소
get_url = ''

# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 

# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

detailList = list()
wait = WebDriverWait(driver, 10)

time.sleep(2)
count = driver.find_element(By.CLASS_NAME, 'psw-t-body.psw-c-t-2').text
count = count.split('/')
count = count[1]
count = int(count[:2])


print(count)

# 한 페이지에 최대 24개의 게임 타이틀 노출
# count가 0으로 딱 떨어지지 않은 경우는 전부 pageCount에 + 1
if count % 24 == 0: 
    pageCount = int(count / 24)
else: pageCount = int(count / 24) + 1

print(f'페이지 수 {pageCount}')
print(f'총 {count}개 게임 수집 시작')


gameList = page_scrap(driver, driver_eng, pageCount)

for i in range(0, len(gameList)):
    result = scrap_detail(driver, driver_eng, gameList[i]['url'], gameList[i]['url'].replace('ko-kr','en-us'))
    detailList.append(result)

playstation_concat(gameList, detailList, "playstation")