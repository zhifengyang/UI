import unittest
from selenium import webdriver
import time

class Init(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://fanyi.youdao.com/')
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(1)
        self.driver.switch_to.frame(2)

    def tearDown(self):
        self.driver.quit()
