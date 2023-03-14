import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test = webdriver.Chrome()
# test.implicitly_wait(5)

"""implicity_wait -> se activeaza cand cauta un element si nu il gaseste,
sistemul asteapta 5 sec si daca nu il gaseste da eroare,
daca il gaseste executa si trece mai departe"""

test.get('https://the-internet.herokuapp.com/login')
test.maximize_window()

test.find_element(By.ID, 'username').send_keys('babau')
# time.sleep(3)

#expected condition
password = WebDriverWait(test, 5).until(EC.presence_of_element_located((By.ID,'password')))
password.send_keys('jshkasfak')

test.find_element(By.ID, 'password').send_keys('jshkasfak')
# am scris gresit pt implicity ways ca sa dea eroare

# time.sleep(3)

quit()