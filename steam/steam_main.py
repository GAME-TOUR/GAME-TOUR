from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from steam_GameListCrawling import scrap_gameList
from steam_concat           import steam_data

def steam_crawling(driver, driver_eng):

    # 게임 목록 크롤링
    gameList = scrap_gameList(driver)

    # 성인 인증 미리 받기 
    adult_cert(driver, driver_eng)

    # 게임 세부정보 크롤링 
    infoList = []

    for i in range(len(gameList)):
        res = gameInfo_scrap(driver, driver_eng, gameList[i]['url'])

        if res != None:
            infoList.append(res)
    
    # 게임 목록, 세부정보 MERGE 
    steam_data(gameList, infoList, "STEAM")
    

# 스팀 상점 페이지 주소 (한국어&영어)
get_url = "https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1"

opt = Options()

# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 

# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

steam_crawling(driver, driver_eng)