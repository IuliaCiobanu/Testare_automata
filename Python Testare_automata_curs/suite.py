import unittest
from alerts import Alerts #fisierul meu

#package pt generarea unui raport
import HtmlTestRunner
from contex import Context_Menu
from firefox_auth import Firefox
from keys import Key

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Context_Menu),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Firefox),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Key)])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Execution Report',
            report_name='Test Result')
        runner.run(test_derulat)

