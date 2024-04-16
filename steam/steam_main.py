from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from Steam.steam_GameInfoCrawling import adult_cert, gameInfo_scrap
from Steam.steam_GameListCrawling import scrap_gameList
from Database.concat              import concat_data


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
    concat_data(gameList, infoList, "STEAM")






