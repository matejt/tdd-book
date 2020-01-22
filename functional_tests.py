import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        binary = r'C:\Users\dhdyk0\AppData\Local\Mozilla Firefox\firefox.exe'
        options = Options()
        options.binary = binary

        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True

        self.browser = webdriver.Firefox(capabilities=cap, options=options)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
