from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def page_scrap(driver, driver_eng, pageNum):
  
  pageList = list()
  
  for _ in range(1, pageNum+1):
    time.sleep(2)
    
    gameGrid = driver.find_element(By.CLASS_NAME, 'psw-grid-list.psw-l-grid')
    games = gameGrid.find_elements(By.TAG_NAME, 'li')
    
    for game in games:
        
        title = game.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME,'section').find_element(By.CLASS_NAME, 'psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2').text
        url = game.find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME, 'a').get_attribute('href')
        pageGame = {
            'title': title,
            'url': url
        }
        
        pageList.append(pageGame)
    
    print(len(pageList))
    
    
    nextBtn = driver.find_element(By.CLASS_NAME, 'psw-icon.psw-icon--chevron-right.psw-icon.psw-icon-size-2.psw-icon--chevron-right').click()
    print('nextBtn clicked!')
    
  return pageList
    