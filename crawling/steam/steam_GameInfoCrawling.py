from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

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


# 해당 페이지 게임 상세정보 스크래핑 
def gameInfo_scrap(driver, driver_eng, url):

    tagLi   = []
    infoLi  = [] 
    titleLi = []
    scrLi   = []

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

    parser = url.split('/')
    for i in range(len(parser)):
        if (parser[i] == 'app'):
            app_id = parser[i+1]

    thumb = f'https://steamcdn-a.akamaihd.net/steam/apps/{app_id}/library_600x900_2x.jpg'
    # 스크린샷
    screenshot = driver.find_elements(By.CLASS_NAME, 'highlight_strip_item.highlight_strip_screenshot')
    for scr in screenshot:
        scrLi.append(scr.find_element(By.TAG_NAME, 'img').get_attribute('src'))


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
        'title': ",".join(titleLi),
        'description': description,
        'company': company,
        'publisher': publisher,
        'thumb': thumb,
        'screenshot': ",".join(scrLi), # 스크린샷 수집? 
        'platform': "steam"
    }
    
    print(Info_dic)