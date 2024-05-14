from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from steam_GameListCrawling import scrap_gameList
from steam_concat           import steam_concat

def steam_crawling(driver, driver_eng):

    # 게임 목록 크롤링
    gameList = scrap_gameList(driver)
    print("gameLsit collect sucess")

    # 성인 인증 미리 받기 
    adult_cert(driver, driver_eng)
    print("adult certification seucess")

    # 게임 세부정보 크롤링 
    infoList = []

    for i in range(len(gameList)):
        res = gameInfo_scrap(driver, driver_eng, gameList[i]['url'])

        if res != None:
            infoList.append(res)
    
    print(infoList)
    # 게임 목록, 세부정보 MERGE 
    steam_concat(gameList, infoList, "STEAM")