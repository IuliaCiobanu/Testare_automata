import unittest

#package pt generarea unui raport
import HtmlTestRunner
from Tema9 import Login

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests( [unittest.defaultTestLoader.loadTestsFromTestCase( Login )] )

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Execution Report2',
            report_name='Test2 Result')
        runner.run(test_derulat)

