from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrap_steam(driver): 
    gameLi = list()
    doScroll = True

    # 현재 높이 저장
    curpageHeight = driver.execute_script('return document.body.scrollHeight')

    # 로딩할 페이지가 있는동안 
    while(doScroll):
        # 페이지 끝으로 이동
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 로딩 대기 
        time.sleep(1)

        # 새로 이동한 높이
        newpageHght = driver.execute_script('return document.body.scrollHeight')

        if curpageHeight == newpageHght:
            doScroll  = False
            break

        curpageHeight = newpageHght

        gameRows = driver.find_element(By.ID, 'search_resultsRows')
        games = gameRows.find_elements(By.TAG_NAME, 'a')

        for i in range(len(gameLi), len(games)):
            title = games[i].find_element(By.CLASS_NAME, 'title').text
            url = games[i].get_attribute('href')
            releaseDate = games[i].find_element(By.CLASS_NAME, 'col.search_released.responsive_secondrow').text

            my_game = {
                'title': title,
                'url': url,
                'date': releaseDate
            }
            gameLi.append(my_game)
    
    return gameLi
