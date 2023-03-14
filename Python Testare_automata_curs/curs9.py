# Locators in Selenium:
# ID,name, class,partial link,CSS,xPath
# ID
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_page=webdriver.Chrome() #Chrom este clasa din pachetul Selenium
chrome_page.get("https://the-internet.herokuapp.com/login") #accesarea liniei de cod dorite
# time.sleep(5)

chrome_page.find_element(By.ID,"username").send_keys("Ramona")
chrome_page.find_element(By.ID,"password").send_keys("parola")
chrome_page.find_element(By.TAG_NAME,"button").click()
chrome_page.find_element(By.LINK_TEXT,"Elemental Selenium").click()
chrome_page.find_element(By.PARTIAL_LINK_TEXT,"Elemental").click() #cand nu e textul complet
time.sleep(5)

chrome_page.quit() #inchide toata instanta browseru-lui => de preferat



# chrome_page.close() inchide un sigur tab -cel activ in instanta de browser