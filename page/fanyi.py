from base.basePage import *
from selenium.webdriver.common.by import By

class Fanyi(WebDriver):
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    login_loc = (By.LINK_TEXT, '登  录')
    loginError_loc = (By.CLASS_NAME, 'ferrorhead')

    def typeUserName(self, username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassWord(self, password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassWord(password)
        self.clickLogin

    @property
    def getLoginError(self):
        return self.findElement(*self.loginError_loc).text
