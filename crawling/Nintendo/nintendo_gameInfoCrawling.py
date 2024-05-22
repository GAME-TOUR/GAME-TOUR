from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from nintendo_gameListCrawling import scrap_gameList, popup_close # test code

def get_description(driver):
    rawTextList = []
    description = None
    descRaw = driver.find_element(By.CLASS_NAME, 'product-attribute-content.expanded').find_elements(By.TAG_NAME,'p')
    
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
    # popup_close(driver) # test code 

    title = driver.find_element(By.CLASS_NAME, 'page-title').find_element(By.TAG_NAME,'span').find_element(By.TAG_NAME,'span').text
    releaseDate = driver.find_element(By.CLASS_NAME, 'product-attribute.release_date').find_element(By.CLASS_NAME, 'product-attribute-val').text
    description = get_description(driver)
    company = driver.find_element(By.CLASS_NAME,'product-attribute.publisher').find_element(By.CLASS_NAME, 'product-attribute-val').text
    tagList = get_tag(driver)
    scrList = get_image(driver)
    thumb = scrList[0]

    info_dic = {
        'thumb': thumb,
        'title': title,
        'date': releaseDate,
        'description': description,
        'company': company,
        'screenshot': ",".join(scrList),
        'tag': ",".join(tagList),
        'platform': "nintendo"
    }

    print(info_dic)
    return info_dic

opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)
url = 'https://store.nintendo.co.kr/70010000054301'

dic = gameinfo_scrap(driver, url)
print(dic)