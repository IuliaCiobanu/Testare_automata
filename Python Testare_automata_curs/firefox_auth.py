import unittest
from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from webdriver_manager.firefox import GeckoDriverManager

# te ajuta sa dea click dreapta

class Firefox(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        # self.firefox = webdriver.Firefox( executable_path=GeckoDriverManager().install() )
        self.firefox = webdriver.Firefox()

        self.firefox.get( "https://the-internet.herokuapp.com/context_menu" )
        self.firefox.maximize_window()


    def tearDown(self) -> None:
        self.firefox.quit()

    def test_contexmenu(self):
        self.firefox.get("https://"+ self.USERNAME + ":" + self.PASSWORD + "@" + "the-internet.herokuapp.com/context_menu")
        time.sleep(3)
