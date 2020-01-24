import time
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy coffee!" into a text cox
        inputbox.send_keys('Buy coffee!')

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy coffee!" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy coffee!' for row in rows),
            'New to-do item did not appear in table'
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
