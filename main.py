from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from steam.steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from steam.steam_GameListCrawling import scrap_gameList
from steam.steam_main import steam_crawling


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


# 스팀 크롤링
steam_crawling(driver, driver_eng)

