from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from nintendo_gameListCrawling import scrap_gameList, popup_close # test code
from nintendo_concat           import nintendo_concat             # test code 
from datetime import datetime
import pandas as pd

def get_description(driver):
    rawTextList = []
    description = None
    try:
        descRaw = driver.find_element(By.CLASS_NAME, 'product-attribute-content.expanded').find_elements(By.TAG_NAME,'p')
        # descRaw = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/p[3]").text
        # return descRaw
    except NoSuchElementException:
        descRaw = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]").text
        return descRaw
    
    if descRaw != []:
        for raw in descRaw:
            rawTextList.append(raw.text)
            description = "\n\n".join(rawTextList)
        
        return description
    else:
        description = driver.find_element(By.CLASS_NAME, 'product-attribute-content.expanded').text
        return description

def get_image(driver):
    
    imgList = []
    
    driver.find_element(By.CLASS_NAME,'fotorama__img').click()
    
    imgNumber = driver.find_elements(By.CLASS_NAME, 'fotorama__nav__frame.fotorama__nav__frame--thumb')
    print(len(imgNumber))
    
    if len(imgNumber) == 0:
        img = driver.find_element(By.CLASS_NAME, 'fotorama__img--full').get_attribute('src')
        imgList.append(img)
        return imgList
        
    nextBtn = driver.find_element(By.CLASS_NAME, 'fotorama__arr.fotorama__arr--next')
    action = ActionChains(driver)
    for _ in range(len(imgNumber)):
        img = driver.find_element(By.CLASS_NAME, 'fotorama__img--full').get_attribute('src')
        imgList.append(img)
        action.move_to_element(nextBtn).perform()
        nextBtn.click()
        time.sleep(2)
    
    return imgList

def get_tag(driver):
    
    tagRaw = driver.find_element(By.CLASS_NAME,'product-attribute.game_category').find_element(By.CLASS_NAME, 'product-attribute-val').text
    
    try:
        tagRaw = tagRaw.replace(' ','')
        tagList = tagRaw.split(',')
        
    except:
        tagList.append(tagRaw)
        
    return tagList

def gameinfo_scrap(driver, url):

    driver.get(url)
    popup_close(driver) # test code 
    
    driver.implicitly_wait(30)

    title = driver.find_element(By.CLASS_NAME, 'page-title').find_element(By.TAG_NAME,'span').find_element(By.TAG_NAME,'span').text
    # print(title)
    # releaseDate = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[5]/div[2]").text
    # print("CSS: ", releaseDate)
    # date = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[5]/div[2]")
    releaseDate = driver.find_element(By.CLASS_NAME, 'product-attribute.release_date').find_element(By.CLASS_NAME, 'product-attribute-val').text
    # print("XPATH: ", releaseDate)
    description = get_description(driver)
    # print(description)
    # company = driver.find_element(By.CLASS_NAME,'product-attribute.publisher').find_element(By.CLASS_NAME, 'product-attribute-val').text
    company = driver.find_element(By.XPATH,"//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[2]/div[1]/div[2]").text
    # print(company)
    tagList = get_tag(driver)
    # print(tagList)
    
    # scrList = get_image(driver)
    # thumb = scrList[0]

    # OLD
    # description = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]").text
    
    # NEW
    # description = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/p[3]").text
    
    info_dic = {
        # 'thumb': thumb,
        'date': releaseDate,
        # 'description': description,
        'company': company,
        # 'screenshot': ",".join(scrList),
        'tag': ",".join(tagList),
        'platform': "nintendo"
    }

    print(info_dic)
    return info_dic

opt = Options()
# opt.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=opt)
# url = 'https://store.nintendo.co.kr/70010000054301' # OLD
# url = 'https://store.nintendo.co.kr/70010000077702'   # NEW

# dic = gameinfo_scrap(driver, url)

A = {'title': 'Lorelei and the Laser Eyes', 'url': 'https://store.nintendo.co.kr/70010000054301'}
B = {'date': '2024.04.21', 'company': 'Annapurna Interactive', 'tag': '어드벤쳐, 퍼즐', 'platform': 'nintendo'}
A_Li = [A]
B_LI = [B]

A_df = pd.DataFrame(A_Li)
B_df = pd.DataFrame(B_LI)
concatList = pd.concat([A_df, B_df], axis=1, join='inner')

# print(A_df)
# print(B_LI)
print(concatList)

now = datetime.now().strftime('%y.%m.%d %H-%M-%S')
concatList.to_csv('./'+now+'_backup'+'.csv', index=False, encoding='UTF-16')
# test code 
# concatList.to_csv('./'+now+'_backup'+'.csv', index=False, encoding='cp949')
