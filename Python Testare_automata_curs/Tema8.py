import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_page=webdriver.Chrome()
# chrome_page.get("https://phptravels.net/")
#
# search_city = chrome_page.find_element(By.ID, "select2-hotels_city-container")
# print(search_city.text)
#
# check_in = chrome_page.find_element(By.ID, "checkin").click()
#
# flights = chrome_page.find_element(By.ID, "flights-tab").click()
#
# CLASS
#
# box = chrome_page.find_elements(By.CLASS_NAME, "info__desc")
# print(box[1].text)
#
# icon_cars = chrome_page.find_elements(By.CLASS_NAME, "text")
# print(icon_cars[1].text)
# icon_cars[1].click()
#
# lazy = chrome_page.find_element(By.CLASS_NAME, " lazyloaded")
# print(lazy[1].text)

# LINK
#
#
#
# XPATH
chrome_page.get("https://www.techlistic.com/p/selenium-practice-form.html")
cookies = chrome_page.find_element(By.XPATH, '//*[@id="ez-accept-all"]').click()

# lista = chrome_page.find_element(By.XPATH, "//*[@id='post-body-3077692503353518311']/div[1]/div/div/div[6]/ol/li[4]")

# atribut/valoare
# input=chrome_page.find_element (By.XPATH, "//button[@name='submit']").click()
# (By.XPATH,"//*[@placeholder='Enter last name']")

# chrome_page.get("https://jules.app/sign-in")
# forgot = chrome_page.find_element(By.XPATH, "//*[@data-test-id='forgot-password-link']")

# CONTAINS


# open = chrome_page.find_element(By.XPATH, '//span[contains(text(),"Open this link")]')

# list = chrome_page.find_element((By.XPATH, ))
# /div[@class='form-group']/div[3]/input

# password = chrome_page.find_element(By.XPATH, "//input[@placeholder='Enter your password']")

# parent = chrome_page.find_element(By.XPATH, "//*[@id='selenium_commands']/option[2]/parent::select")
# sibling = chrome_page.find_element(By.XPATH, '//*[@id="selenium_commands"]/option[2]/following-sibling::option'

# clase = chrome_page.find_element(By.XPATH, "//*[@class='control-group']/input[@name='firstname']")

sau = chrome_page.find_element(By.XPATH,"//input[@name='firstname'] | //*[@name ='x']").send_keys("Iulia")

# photo = chrome_page.find_element(By.XPATH,'//*[@id="ACCOUNT"]')

# print(photo.get_attribute('id'))
# print(photo.get_attribute('class'))
# print(photo.get_attribute('type'))

# visa = chrome_page.find_element(By.XPATH,'//*[@id="visa-tab"]')
# print(visa.text)
# chrome_page.get("https://jules.app/sign-in")
# experience = chrome_page.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input').send_keys("iulia@yahoo.com")
#
# forgot_password = chrome_page.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/a')
# print(forgot_password.get_attribute('href'))
# time.sleep(3)

# NAME
# checkout = chrome_page.find_element(By.NAME,"checkout").click()
# time.sleep(3)

# chrome_page.get("https://www.techlistic.com/p/selenium-practice-form.html")
# cookies = chrome_page.find_element(By.XPATH, '//*[@id="ez-accept-all"]').click()
# firstname = chrome_page.find_element(By.NAME, 'firstname').send_keys('Iulia')
# lastname = chrome_page.find_element(By.NAME, 'lastname').send_keys('Ciobanu')
# gender =  chrome_page.find_elements(By.NAME,'exp')
# gender[1].click()

# LINK
# chrome_page.get("https://the-internet.herokuapp.com/")
# link1= chrome_page.find_element(By.LINK_TEXT, "A/B Testing").click()
#
# link2= chrome_page.find_element(By.LINK_TEXT, "Basic Auth")
# print(link2.get_attribute('href'))
#
# link3 = chrome_page.find_element(By.LINK_TEXT, "Elemental Selenium")
# print(link3.size)

# Partial Link
# parlink1 = chrome_page.find_element(By.PARTIAL_LINK_TEXT, "Infin")
# print(parlink1.text)
#
# parlink2 = chrome_page.find_element(By.PARTIAL_LINK_TEXT, "Shift")
# print(parlink2.text)
# parlink2.click()
#
# parlink3 = chrome_page.find_element(By.PARTIAL_LINK_TEXT, "Ty")
# print(parlink3.size)

# Tags
# chrome_page.get("https://www.techlistic.com/p/selenium-practice-form.html")
# cookies = chrome_page.find_element(By.XPATH, '//*[@id="ez-accept-all"]').click()
#
# inputs_list = chrome_page.find_elements(By.TAG_NAME, 'input')
# print(inputs_list[0].get_attribute("name"))
#
# buttons_list = chrome_page.find_elements(By.TAG_NAME, 'button')
# print(buttons_list[0].get_attribute('class'))
#
# lista = chrome_page.find_elements(By.TAG_NAME, 'link')
# print(lista[3].get_attribute('href'))

# CSS

# account = chrome_page.find_element(By.CSS_SELECTOR,'button[id="ACCOUNT"]').click()
# checkin= chrome_page.find_element(By.CSS_SELECTOR, '#checkout')
# checkin = chrome_page.find_elements(By.CSS_SELECTOR, '.nav-link text-start text-capitalize  waves-effect')


time.sleep(3)
chrome_page.quit()
