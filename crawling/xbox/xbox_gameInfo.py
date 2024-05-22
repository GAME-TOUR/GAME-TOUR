from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import pandas as pd
import datetime
import time

def find_bundle(driver, driver_eng):
    bundleList = []
    tmp_title = ''
    tmp_url = ''
    try:
        bundleList = driver.find_element(By.CSS_SELECTOR,"section[aria-label='이 번들']").find_element(By.CSS_SELECTOR, "div[class='ModuleRow-module__row___N1V3E']").find_element(By.CSS_SELECTOR, "ol[class='ItemsSlider-module__wrapper___nAi6y']").find_elements(By.TAG_NAME, 'li')

        bundleList.pop()
        print(bundleList)
        
        print(len(bundleList))
        for titles in bundleList:
            title = titles.find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME,'div').find_element(By.TAG_NAME,'a').get_attribute('title')
            link = titles.find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME,'div').find_element(By.TAG_NAME,'a').get_attribute('href')


            title = title.replace('Xbox Series X|S용 ','').replace('Xbox One용 ','').replace(' Xbox One', '').replace(' Xbox Series X|S','')

            print(title)
            if tmp_title == '':
                tmp_title = title
                tmp_url = link
                

            elif len(title) < len(tmp_title):
                
                tmp_title = title
                tmp_url = link
            
            print(tmp_title)
            
        print(tmp_title)
        print(tmp_url)
        driver.get(tmp_url)
        driver_eng.get(tmp_url.replace('ko-KR', 'en-us'))
        time.sleep(10)
        
        
        
    except NoSuchElementException:
        print("this is not bundle")
        
        return None

def get_tag(driver):
    ele = driver.find_element(By.CSS_SELECTOR, "div[class='typography-module__xdsSubTitle1___N02-X ProductInfoLine-module__productInfoLine___Jw2cv']")
    tagRaw = ele.find_element(By.TAG_NAME, "span").text
    
    tagRaw = tagRaw.replace('및', '•').replace(' ','')
    
    tagList = tagRaw.split('•')
    
    del tagList[0]
    
    #print(tagList)
    return tagList

def scrap_gameinfo(driver, driver_eng, url_ko, url_en):
  
  driver.implicitly_wait(10)
  driver_eng.implicitly_wait(10)
  
  driver.get(url_ko)
  driver.get(url_en)
  
  find_bundle(driver, driver_eng)
  
  title = driver.find_element(By.CSS_SELECTOR, "h1[data-testid='ProductDetailsHeaderProductTitle']").text
  
  try:
      engTitle = driver_eng.find_element(By.CSS_SELECTOR, "h1[data-testid='ProductDetailsHeaderProductTitle']").text
  except NoSuchElementException:
      engTitle = title
  titleList = [title, engTitle]
  titleList = sorted(set(titleList))
      
  description = driver.find_element(By.CSS_SELECTOR, "p[class='Description-module__description___ylcn4 typography-module__xdsBody2___RNdGY ExpandableText-module__container___Uc17O']").text
  company = driver.find_element(By.CSS_SELECTOR, "div[class='typography-module__xdsBody2___RNdGY']").text
  tagList = get_tag(driver)
  
  info_dic = {
    'tag': ",".join(tagList),
    'title': ",".join(titleList),
    'description': description,
    'company': company,
    'platform': 'xbox'
  }
  
  return info_dic