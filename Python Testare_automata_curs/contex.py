import unittest
from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# te ajuta sa dea click dreapta

class Context_Menu(unittest.TestCase):
    USERNAME = (By.ID, 'username')
    BOX = (By.ID, 'hot-spot')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get( "https://the-internet.herokuapp.com/context_menu" )
        self.chrome.maximize_window()
        self.chrome.implicitly_wait( 2 )

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_contexmenu(self):
        action = ActionChains (self.chrome)
        elem = self.chrome.find_element(*self.BOX)
        action.context_click(elem).perform()
        time.sleep(2)
        alert = self.chrome.switch_to.alert
        text = alert.text
        assert text == 'You selected a context menu', f"Error: NU MERGE"
        alert.accept()