from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from splinter import Browser


def load_page(browser, page=''):
    host_page = 'http://localhost:8000'
    return(browser.get(host_page+page))



class NewGametest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        load_page(self.browser)
        self.assertIn('ML-TTT', self.browser.title)
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual("Welcome to TicTacToe Man vs. Machine!", header)


    def test_links(self):
        load_page(self.browser)
        image = self.browser.find_element_by_xpath("//img[@title='github']")
        image.click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, 'https://github.com/simontanner/machine-learning')

    def test_play_button(self):
        load_page(self.browser)
        button = self.browser.find_element_by_name("playGame")
        button.click()
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual('Play the Machine', header)

    def test_can_enter_their_name(self):
        load_page(self.browser, '/playgame')
        submit_name = self.browser.find_element_by_name("player_name")
        submit_name.send_keys('Simon')
        submit_name.send_keys(Keys.ENTER)
        time.sleep(5)
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual('Simon vs. Machine', header)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
