import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_page=webdriver.Chrome()
chrome_page.get("https://the-internet.herokuapp.com/login")

# # //*[text()="Click for JS Alert"] - @ se pune la toate mai putin la text

# /html/body/div[2]/div/div/form/div[1]/div/input  --full xpath

# //*[@id="username"] - relativ xpath - porneste de la taggul input- cea mai folosita

chrome_page.find_element(By.XPATH,'//*[@id="username"]').send_keys("iulia")
time.sleep(2)

# * - select all, tine locul unui tag cum ar fi: input,div,form - precedat de [@atribut="valoare"] === //*[@atribut="valoare"]
chrome_page.find_element(By.XPATH,'//*[@type="text"]').send_keys("zazu")
time.sleep(2)

chrome_page.find_element(By.XPATH,'//input[@type="password"]').send_keys("mitzighdfhfxh")
time.sleep(2)

# # xpath cu keywordul "contains" //input[contains(@name,"pass")] - aici name este atribut
# //input[contains(text(),"Log")]



# //i[text()=" Login")]
# //i[text()=" Login"]/parent::button - navigarea din parinte inspre copil de face cu un slash
# navigarea catre un urmas care nu este urmas direct se face cu //
# navigarea in sens invers la fratele anterior  -> /preceding-sibiling::tag

# parint:: - cand vrem sa navigam in sus
chrome_page.sleep()