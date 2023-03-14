from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#pt explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(TestCase):
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get( "https://the-internet.herokuapp.com/login" )
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_1(self):
        self.chrome.get( "https://the-internet.herokuapp.com/" )
        self.chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(3)
        actual_url = self.chrome.current_url
        print(actual_url)
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, f"Error: {expected_url}, actual {actual_url}"

    def test_2(self):
        # self.chrome.get("https://the-internet.herokuapp.com/login")
        page_title = self.chrome.title
        time.sleep(3)
        expected_title = "The Internet"
        assert page_title == expected_title, f"Error: expected title: {expected_title} and actual page title: {page_title}"

    def test_3(self):
        # self.chrome.get( "https://the-internet.herokuapp.com/login" )
        h2_text = self.chrome.find_element(By.XPATH, "//h2").text
        time.sleep(3)
        h2_expected="Login Page"
        assert h2_text == h2_expected, f"Error: {h2_text} DESI AS VREA {h2_expected}"

    def test_4(self):
        log_button = self.chrome.find_element(By.TAG_NAME, "button").is_displayed()
        assert log_button, f"Error: THE BUTTON IS NOT DISPLAYED"

    def test_5(self):
        elemental_selenium = self.chrome.find_element(By.LINK_TEXT, "Elemental Selenium")
        elemental_selenium_href = elemental_selenium.get_attribute("href")
        expected_elemental_selenium_href = "http://elementalselenium.com/"
        assert elemental_selenium_href == expected_elemental_selenium_href, f"Error: THE HREF ATTRIBUTE IS NOT CORRECT "

    def test_6(self):
        username = self.chrome.find_element( By.NAME, "username").clear()
        password = self.chrome.find_element(By.NAME, "password").clear()
        login = self.chrome.find_element(By.TAG_NAME, "button").click()
        alert = self.chrome.find_element(By.ID, "flash")
        time.sleep( 3 )
        actual_alert_msg = alert.text
        expected_alert_msg ='Your username is invalid!\n×'
        assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "


    def test_7(self):
        username = self.chrome.find_element( By.NAME, "username" ).send_keys("dfsdfdag")
        password = self.chrome.find_element(By.NAME, "password").send_keys("sdfdgdf")
        login = self.chrome.find_element(By.TAG_NAME, "button").click()
        alert = self.chrome.find_element(By.ID, "flash")
        time.sleep( 3 )
        actual = alert.text
        expected = 'Your username is invalid!'
        self.assertTrue( expected in actual, 'Error message text is incorrect')

    def test_8(self):
        username = self.chrome.find_element( By.NAME, "username" ).clear()
        password = self.chrome.find_element(By.NAME, "password").clear()
        login = self.chrome.find_element(By.TAG_NAME, "button").click()
        alert = self.chrome.find_element(By.ID, "flash")
        time.sleep( 3 )
        x = self.chrome.find_element(By.CSS_SELECTOR,"a[class='close']").click()
        time.sleep( 3 )
        try:
            self.chrome.find_element( By.ID, "flash" )
        except NoSuchElementException:
            print("NU MAI APARE")

    def test_9(self):
        labels = self.chrome.find_elements(By.CSS_SELECTOR, "label")
        expected_labels_list = ["Username", "Password"]
        for label in labels:
            self.assertTrue( label.text in expected_labels_list, f"{label.text} IS NOT IN THE LIST" )

    def test_10(self):
        username = self.chrome.find_element( By.NAME, "username" ).send_keys("tomsmith")
        password = self.chrome.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
        login = self.chrome.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)
        print(self.chrome.current_url)
        self.assertTrue("secure" in self.chrome.current_url, f"THE NEW URL HAS NO SECURE WORD IN IT")
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.ID,'flash')))
        # la find elem by class imi da eroare
        flash_succes = self.chrome.find_element(By.ID,'flash')
        assert flash_succes.is_displayed(), f"IS NOT DISPLAYED"
        self.assertTrue("secure area!" in flash_succes.text, f"{flash_succes} IS NOT IN THE TEXT")

    def test_11(self):
        username = self.chrome.find_element( By.NAME, "username" ).send_keys( "tomsmith" )
        password = self.chrome.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
        login = self.chrome.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)
        logout = self.chrome.find_element(By.XPATH,"//*[@id='content']/div/a/i").click()
        expected_url="https://the-internet.herokuapp.com/login"
        actual_url=self.chrome.current_url
        assert expected_url==actual_url,f"The URL is not correct"

    def test_12(self):
        username = self.chrome.find_element( By.NAME, "username" )
        h4=self.chrome.find_element(By.CSS_SELECTOR,"h4").text
        words_list=h4.split(" ")
        print(words_list)
        password = self.chrome.find_element( By.NAME, "password" )
        login = self.chrome.find_element( By.TAG_NAME, "button" )
        time.sleep( 2 )

        for word in words_list:
            print(word)
            username.send_keys( "tomsmith" )
            password.send_keys(word)
            time.sleep(3)
            login.click()
            time.sleep( 3 )
            self.chrome.find_element( By.CSS_SELECTOR, "a[class='close']" ).click()
            time.sleep( 3 )

            url = self.chrome.current_url
            print(url)
            if "secure" in url:
                print( f'Password: {password}' )
                break
            else:
                print( f"'{word}' is not the password" )
        assert "secure" in url, f"No password found"
#


