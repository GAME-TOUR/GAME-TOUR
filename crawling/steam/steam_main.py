from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from steam_GameListCrawling import scrap_gameList
from steam_concat           import steam_concat

opt = Options()
# 스팀 상점 페이지 주소 (한국어&영어)
get_url = "https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1"

# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 

# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

# 게임 목록 크롤링
gameList = scrap_gameList(driver)
print("gameLsit collect sucess")

# 성인 인증 미리 받기 
adult_cert(driver, driver_eng)
print("adult certification seucess")

# 게임 세부정보 크롤링 
detailList = []

for i in range(len(gameList)):
    detail = gameInfo_scrap(driver, driver_eng, gameList[i]['url'])

    if detail != None:
        detailList.append(detail)
    
    print(detailList)
    
# 게임 목록, 세부정보 MERGE 
steam_concat(gameList, detailList, "STEAM")