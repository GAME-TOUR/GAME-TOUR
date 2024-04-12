from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from steam.steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from steam.steam_GameListCrawling import scrap_gameList


def steam_crawling(driver, driver_eng):

    gameList = [] 

    # 스팀 게임 목록 
    driver.get("https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1")
    
    # 사이트를 한국어로 전환
    driver.find_element(By.XPATH, '//*[@id="language_pulldown"]').click()
    driver.find_element(By.XPATH, '//*[@id="language_dropdown"]/div/a[4]').click()

    # 언어 전화 로딩 대기
    time.sleep(2)

    # 게임 목록 크롤링
    gameList = scrap_gameList(driver)

    # 성인 인증 미리 받기 
    adult_cert(driver, driver_eng)

    # 게임 세부정보 크롤링 
    gameInfo_scrap(driver, driver_eng)

    # 게임 목록, 세부정보 MERGE 
    

