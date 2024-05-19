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

  games = driver.find_elements(By.CLASS_NAME, 'product.details.category-product-item-info.product-item-details')
  
  for game in games[:51]:
      
    title = game.find_element(By.CLASS_NAME, 'product.name.product-item-name').text
    url = game.find_element(By.CLASS_NAME, 'product-item-link').get_attribute('href')            
    pageGame = {
        'title': title,
        'url': url
    }
        
    gameLi.append(pageGame)
          
  return gameLi

