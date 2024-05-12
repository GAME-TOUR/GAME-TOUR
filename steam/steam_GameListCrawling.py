from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrap_gameList(driver): 
    gameLi = list()
    doScroll = True
    
    # 스팀 게임 목록 
    driver.get("https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1")
    
    # 사이트를 한국어로 전환
    driver.find_element(By.XPATH, '//*[@id="language_pulldown"]').click()
    driver.find_element(By.XPATH, '//*[@id="language_dropdown"]/div/a[4]').click()
    
    # 언어 전화 로딩 대기
    time.sleep(2)

    # 리스트에서 게임만 선택 - DLC, 사운드트랙 등 필요없는 요소들 제거 
    element = driver.find_element(By.XPATH, '//*[@id="additional_search_options"]/div[4]/div[1]/div')
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.XPATH, '//*[@id="narrow_category1"]/div[1]/span').click()
    
    # 대기
    time.sleep(2)

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
            # if my_game['title'] == 'DARK SOULS III Deluxe Edition':
            #     continue
            # if my_game['title'] == 'Fallout 4: Game of the Year Edition':
            #     continue
            # if my_game['title'] == 'Dying Light Enhanced Edition':
            #     continue
            # if my_game['title'] == 'STAR WARS Jedi: Fallen Order Deluxe Edition':
            #     continue
            # if my_game['title'] == 'not available':
            #     continue
            gameLi.append(my_game)

    return gameLi
