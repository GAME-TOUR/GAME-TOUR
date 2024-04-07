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

    tagLi = []
    infoLi = [] 

    driver.implicity_wait(10)
    driver_eng.implicity_wait(10)

    driver.get(url)
    driver.get(url)

    # 태그 수집 
    try:
        tags = driver.find_element(By.CLASS_NAME,'glance_tags.popular_tags').find_elements(By.CLASS_NAME,'app_tag')
    except NoSuchElementException:
        tags = None

    for tag in tags:
        if tag.text != '':
            tagLi.append(tag.text)
    tagLi.remove('+')

    title = driver.find_element(By.ID, 'appHubAppName').text
        