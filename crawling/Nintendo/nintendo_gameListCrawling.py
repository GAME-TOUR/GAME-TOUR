from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def popup_close(driver): 
    
    wait = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='popup-close']")))
    popupClose = driver.find_element(By.CSS_SELECTOR, "button[class='popup-close']")
    popupClose.click()
    
    print('popup closed')

def scrap_gameList(driver):
  
  gameLi = list()
  
  title = driver.find_elements(By.XPATH, '//*[@id="product-item-info_11024"]/div/strong/a')
  url   = driver.find_elements(By.XPATH, '//*[@id="product-item-info_11024"]/div/strong/a')
  
  print(title)
  print(url)
  
  # g = driver.find_elements(By.XPATH, '//*[@id="amasty-shopby-product-list"]')
  # print(g)
  # print(type(g))
  # print(len(g))
  
  # games = driver.find_elements(By.XPATH, '//*[@id="amasty-shopby-product-list"]/div[2]/ol')
  # print(games)
  # print(type(games))
  # print(len(games))

#  for game in games:
    
  #  title = game.find_element(By.XPATH, '//*[@id="product-item-info_11024"]/div/strong/a').text
  #   url   = game.find_element(By.CLASS_NAME, 'category-product-item-title-link').get_attribute('href')
  #   
  #   gm = {
  #     'title': title,
  #     'url': url
  #   }
  #   print(gm)
  #   
  #   gameLi.append(gm)
    
  return gameLi

