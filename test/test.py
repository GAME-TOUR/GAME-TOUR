from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import datetime
import time

# 스팀 상점 페이지 주소 (한국어&영어)
get_url = "https://store.steampowered.com/search/?supportedlang=english%2Ckoreana&filter=topsellers&ndl=1"

opt = Options()

# 브라우저 꺼짐 방지 옵션 - 개발용
# opt.add_experimental_option("detach", True) 

# 불필요한 에러 메시지 삭제 
# opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# 드라이버 설정 
driver = webdriver.Chrome(options=opt)
driver_eng = webdriver.Chrome(options=opt)

# 성인 인증 절차를 미리 해결 
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
    # while(doScroll):
    #     # 페이지 끝으로 이동
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #     # 로딩 대기 
    #     time.sleep(1)

    #     # 새로 이동한 높이
    #     newpageHght = driver.execute_script('return document.body.scrollHeight')

    #     if curpageHeight == newpageHght:
    #         doScroll  = False
    #         break

    #     curpageHeight = newpageHght

    #     gameRows = driver.find_element(By.ID, 'search_resultsRows')
    #     games = gameRows.find_elements(By.TAG_NAME, 'a')

    #     for i in range(len(gameLi), len(games)):
    #         title = games[i].find_element(By.CLASS_NAME, 'title').text
    #         url = games[i].get_attribute('href')
    #         releaseDate = games[i].find_element(By.CLASS_NAME, 'col.search_released.responsive_secondrow').text

    #         my_game = {
    #             'title': title,
    #             'url': url,
    #             'date': releaseDate
    #         }
    #         gameLi.append(my_game)

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

# 해당 페이지 게임 상세정보 스크래핑 
def gameInfo_scrap(driver, driver_eng, url):

    tagLi = []
    infoLi = [] 
    titleLi = []

    driver.implicitly_wait(2)
    driver_eng.implicitly_wait(2)

    driver.get(url)
    driver_eng.get(url)

    # 태그 수집 
    try:
        tags = driver.find_element(By.CLASS_NAME,'glance_tags.popular_tags').find_elements(By.CLASS_NAME,'app_tag')
    except NoSuchElementException:
        print("It's compilation")
        tags = None
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

    # 게임 정보
    description = driver.find_element(By.CLASS_NAME, 'game_description_snippet').text
    
    Info_dic = {
        'tag': ",".join(tagLi),
        'K-E': ",".join(titleLi),
        'description': description,
        'company': company,
        'publisher': publisher,
        # 'screenshot': ",".join(scrLi), -- 스크린샷 수집? 
        'platform': "steam"
    }
    print(Info_dic)

def concat_data(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)
    
    now = datetime.datetime.now().strftime('%y.%m.%d %H-%M-%S')

    concatList = pd.concat([gameList_df, infoList_df])
    concatList.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False, encoding='cp949')

    return concatList

smp = scrap_gameList(driver)
print(smp)
adult_cert(driver, driver_eng)

tmp = []
for i in range(len(smp)):
    # print(smp[i]['url'])
    res = gameInfo_scrap(driver, driver_eng, smp[i]['url'])
    
    if res != None:
        tmp.append(res)

concat_data(smp, tmp, 'steam') 

time.sleep(10)

# concat_data(smp, )
# smp_df = pd.DataFrame(smp)
# print(smp_df)
# gameInfo_scrap(driver, driver_eng, 'https://store.steampowered.com/app/281990/Stellaris/')

# A = {
#     'title': "스텔라리스",
#     'url': "https://store.steampowered.com/app/281990/Stellaris/",
#     'date': "2016년 5월 10일"
# }
# ALi = list()
# ALi.append(A)
# 
# tagLi = ['Space', 'Grand Strategy']
# titleLi = ['스텔라리스', 'Stellaris']
# B = {
#     'tag': ",".join(tagLi),
#     'KOR-ENG': ",".join(titleLi),
#     'description': "항성간 여행을 통해 우주를 탐험하며 수많은 종족들도 만나보세요. 과학선을 보내 우주를 조사하고 탐험하면서 은하 제국을 건설하고, 건축선을 보내 새로 발견한 행성에 기지를 건설하세요. 소속 사회를 위한 탐험에 나서 매장된 보물과 은하계의 경이를 발견하고, 탐험가의 한계치와 진화 범위를 설정하세요",
#     'company': "Paradox Development Studio",
#     'publisher': "Paradox Interactive",
#     # 'screenshot': ",".join(scrLi), -- 스크린샷 수집? 
#     'platform': "steam"
# }
# BLi = list()
# BLi.append(B)
# 
# adf = pd.DataFrame(ALi)
# bdf = pd.DataFrame(BLi)
# now = datetime.datetime.now().strftime('%y.%m.%d %H-%M-%S')
# print(now)
# platform = 'steam'
# # print(adf)
# # print(bdf)
# concatLi = pd.concat([adf, bdf], axis=1, join='inner')
# concatLi.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False, encoding='cp949')
# print(concatLi) 