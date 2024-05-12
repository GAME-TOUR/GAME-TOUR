from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import time

# 스팀 상점 페이지 주소 (한국어&영어)
get_url = "https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1"

opt = Options()

# 브라우저 꺼짐 방지 옵션 - 개발용
opt.add_experimental_option("detach", True) 

# 불필요한 에러 메시지 삭제 
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

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
            if my_game['title'] == 'DARK SOULS III Deluxe Edition':
                print("Yes1")
            if my_game['title'] == 'Fallout 4: Game of the Year Edition':
                print("Yes2")
            if my_game['title'] == 'Dying Light Enhanced Edition':
                print("Yes3")
            if my_game['title'] == 'STAR WARS Jedi: Fallen Order Deluxe Edition':
                print("Yes4")
            if my_game['title'] == 'not available':
                print("YES5")
            if my_game['title'] == "Europa Universalis IV":
                print(my_game['url'])
                print("YES6")
            
            # print(my_game)
            gameLi.append(my_game)

    return gameLi

def adult_cert(driver, driver_eng): 

    # 성인 인증이 필요한 게임 페이지
    driver.get('https://store.steampowered.com/agecheck/app/553850/')
    driver_eng.get('https://store.steampowered.com/agecheck/app/553850/')

    time.sleep(1)
    
    driver.find_element(By.ID, 'ageYear').click()
    driver_eng.find_element(By.ID, 'ageYear').click()

    time.sleep(1)


    driver.find_element(By.XPATH, '//*[@id="ageYear"]/option[101]').click()
    driver_eng.find_element(By.XPATH, '//*[@id="ageYear"]/option[101]').click()

    time.sleep(1)

    driver.find_element(By.ID, 'view_product_page_btn').click()
    driver_eng.find_element(By.ID, 'view_product_page_btn').click()

    time.sleep(2)

# 해당 페이지 게임 상세정보 스크래핑 
def gameInfo_scrap(driver, driver_eng, url):

    tagLi = []
    infoLi = [] 
    titleLi = []

    driver.implicitly_wait(2)
    driver_eng.implicitly_wait(2)

    driver.get(url)
    driver_eng.get(url)

    # driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[1]/div[1]/div[3]/div').click()
    # driver_eng.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[1]/div[1]/div[3]/div').click()
    

    # 태그 수집 
    try:
        tags = driver.find_element(By.CLASS_NAME,'glance_tags.popular_tags').find_elements(By.CLASS_NAME,'app_tag')
    except NoSuchElementException:
        tags = None
        print("Compilation")
        return 

    for tag in tags:
        if tag.text != '':
            tagLi.append(tag.text)
    tagLi.remove('+')

    # 제목 수집 / 영문 이름 수집
    title = driver.find_element(By.ID, 'appHubAppName').text
    title_en = driver_eng.find_element(By.ID, 'appHubAppName').text
    titleLi.append(title)
    titleLi.append(title_en)
    # 한글/영문 이름이 동일할 수 있으니 중복 제거 
    titleLi = sorted(set(titleLi))

    # 개발사 정보 수집
    company = driver.find_element(By.XPATH, '//*[@id="developers_list"]/a').text

    # 배급사 정보 수집 
    try: 
      publisher = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[1]/div/div[3]/div[4]/div[2]/a').text
    except NoSuchElementException:
      publisher = driver.find_element(By.XPATH, '//*[@id="game_highlights"]/div[2]/div/div[3]/div[4]/div[2]/a').text
    # //*[@id="game_highlights"]/div[1]/div/div[3]/div[4]/div[2]/a 

    # 게임 정보
    description = driver.find_element(By.CLASS_NAME, 'game_description_snippet').text
    
    Info_dic = {
        'tag': ",".join(tagLi),
        'title': ",".join(titleLi),
        'description': description,
        'company': company,
        'publisher': publisher,
        # 'screenshot': ",".join(scrLi), -- 스크린샷 수집? 
        'platform': "steam"
    }

    print(Info_dic)
  

# smp = list()
# smp = scrap_gameList(driver)
# print(smp)

# smp_df = pd.DataFrame(smp)

# print(smp_df)
#adult_cert(driver, driver_eng)
gameInfo_scrap(driver, driver_eng, 'https://store.steampowered.com/app/2326590/Kakuriyo_Village_Moratorium_of_Adolescence/')
