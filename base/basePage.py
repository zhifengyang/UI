from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        '''定位单个元素的方法'''
        try:
            # return self.driver.find_element(*loc)
            return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findsElenemt(self, *loc):
        '''定位多个元素的方法'''
        try:
            # return self.driver.find_elements(*loc)
            return WebDriverWait(self.driver, 20).until(lambda  x: x.find_elements(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))