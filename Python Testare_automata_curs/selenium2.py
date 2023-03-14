import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_page=webdriver.Chrome()
chrome_page.get("https://the-internet.herokuapp.com/login")

chrome_page.find_element(By.TAG_NAME,"form")

# ----------------------------

chrome_page.find_element(By.CSS_SELECTOR,'form > div [type="text"]').send_keys("dan")
time.sleep(2)
chrome_page.find_element(By.CSS_SELECTOR,'form >div:nth-of-type(1) input').clear()
# chrome_page.find_element(By.CSS_SELECTOR,'form >div:nth-of-type(1) input').send_keys(Keys.CONTROL+"a")#alta varianta pt clear

chrome_page.find_element(By.CSS_SELECTOR,'form >div:nth-of-type(1) input').send_keys("adela")
chrome_page.find_element(By.CSS_SELECTOR,'form >div:nth-of-type(1) input').clear()

# -----------------------------
#tipareste parola
chrome_page.find_element(By.CSS_SELECTOR,'form >div:last-of-type input').send_keys("iulia")
chrome_page.find_element(By.CSS_SELECTOR,'form >div:nth-of-type(1) input').clear()
time.sleep(2)

chrome_page.find_element(By.CSS_SELECTOR,'form >div:first-of-type input').send_keys("fdgdfgfd")
time.sleep(2)
chrome_page.find_element(By.XPATH,'//*[@id="username"]').send_keys("iulia")
time.sleep(2)

chrome_page.quit()