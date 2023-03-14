
# Folosirea librariei unitest

# Metoda de set-up - Adica - pasi care se fac inainte de executarea testului"

# Toate metodele de testare trebuie sa aiba in fata 'test_' altfel nu il recunoaste
# Tear-Down - toti pasii de dupa executare - ex:quit()

# import unittest - pt tot pachetul
import unittest
from unittest import TestCase

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Definirea metodei de setup

class Alerts(TestCase):
    ALERT_BUTTON = (By.XPATH, '//*[text()="Click for JS Alert"]')
    CONFIRM_BUTTON = (By.XPATH, '//*[text()="Click for JS Confirm"]')
    PROMPT_BUTTON = (By.XPATH, '//*[text()="Click for JS Prompt"]')
    ALERT_MSG = (By.ID, "result")
# Definirea metodei de setUp
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
# Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()

    # def test_alert_accept(self):
    #     self.chrome.find_element(*self.ALERT_BUTTON).click()
    #     time.sleep(5)
    #     js_alert = self.chrome.switch_to.alert
    #     js_alert.accept()  # built-in method care accepta alerta e.g. da click pe buton
    #     actual_alert_msg = self.chrome.find_element(*self.alert_msg).text
    #     expected_alert_msg = "You successfully clicked an alert"
    #     assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "
    #
    # def test_confirm_accept(self):
    #     self.chrome.find_element(* self.CONFIRM_BUTTON).click()
    #     js_confirm = self.chrome.switch_to.alert
    #     js_confirm.accept()
    #     actual_alert_msg = self.chrome.find_element( *self.ALERT_MSG ).text
    #     expected_alert_msg = "You clicked: Ok"
    #     assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

    # def test_confirm_cancel(self):
    #     self.chrome.find_element(* self.CONFIRM_BUTTON).click()
    #     js_confirm = self.chrome.switch_to.alert
    #     js_confirm.dismiss()
    #     actual_alert_msg = self.chrome.find_element( *self.ALERT_MSG ).text
    #     print(actual_alert_msg)
    #     expected_alert_msg = "You clicked: Cancel"
    #     assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

    # def test_prompt_no_text_accept(self):
    #     self.chrome.find_element(*self.PROMPT_BUTTON).click()
    #     js_prompt = self.chrome.switch_to.alert
    #     js_prompt.accept()
    #     actual_alert_msg = self.chrome.find_element( *self.ALERT_MSG ).text
    #     expected_alert_msg = "You entered:"
    #     assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

    @unittest.skip #ca dau skit la un test
    def test_prompt_no_text_dismiss(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.dismiss()
        actual_alert_msg = self.chrome.find_element( *self.ALERT_MSG ).text
        expected_alert_msg = "You entered: null"
        assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

    def test_prompt_no_text_null(self):
        self.chrome.find_element( *self.PROMPT_BUTTON ).click()
        js_prompt = self.chrome.switch_to.alert
        js_prompt.send_keys( "TEXTUL INTRODUS DE MINE" )
        js_prompt.dismiss()
        actual_alert_msg = self.chrome.find_element( *self.ALERT_MSG ).text
        expected_alert_msg = "You entered: null"
        assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "
