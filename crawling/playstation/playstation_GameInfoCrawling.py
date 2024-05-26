import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def scrap_detail(driver, driver_eng, url_kr, url_en):
  
  titleList = list()
  
  driver.get(url_kr)
  driver_eng.get(url_en)
  
  tags = driver.find_element(By.CSS_SELECTOR, "dd[data-qa='gameInfo#releaseInformation#genre-value']").text
  tagList = tags.split(',')
  
  thumb = driver.find_element(By.XPATH, '/html/body/div[3]/main/div/div[1]/div[1]/div/div/div/div/span/img[2]').get_attribute('src')
  description = driver.find_element(By.CSS_SELECTOR, "div[class='psw-l-w-1/1 psw-l-w-2/3@tablet-s psw-l-w-2/3@tablet-l psw-l-w-1/2@laptop psw-l-w-1/2@desktop psw-l-w-1/2@max']").find_element(By.TAG_NAME, 'p').text
  company = driver.find_element(By.CSS_SELECTOR, "dd[data-qa='gameInfo#releaseInformation#publisher-value']").text
  releaseDate = driver.find_element(By.CSS_SELECTOR, "dd[data-qa='gameInfo#releaseInformation#releaseDate-value']").text
  
  try:
      title_en = driver_eng.find_element(By.CSS_SELECTOR, "h1[data-qa='mfe-game-title#name']").text    
  except NoSuchElementException:
      title_en = None

  title = driver.find_element(By.CSS_SELECTOR, "h1[data-qa='mfe-game-title#name']").text
  
  if title_en != None:
    titleList.append(title_en)
    
  titleList.append(title)
  titleList = sorted(set(titleList))
  
  info_dic = {
    'date': releaseDate,
    'title': ",".join(titleList),
    'description': description,
    'thumb': thumb, 
    'company': company,
    'tag': ",".join(tagList),
    'platform': "playstation"
  }
  
  print(info_dic)
  return info_dic