from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):

    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    EROR_MESSAGE = (By.XPATH,"//div[@class='oxd-alert-content oxd-alert-content--error']")
    USERNAME_REQUIRED = (By.XPATH,"//form[@class='oxd-form']/div[1]//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
    PASSWORD_REQUIRED = (By.CSS_SELECTOR,".oxd-form > div:nth-of-type(2) .oxd-text")

    def openURL(self):
        self.open_url(ConfigReader.get_base_url())

    def input_username(self,username):
        self.type(self.USERNAME_INPUT,username)

    def input_password(self,password):
        self.type(self.PASSWORD_INPUT,password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def pesan_eror(self):
        return self.get_text(self.EROR_MESSAGE)

    def erorinput_username(self):
        return self.get_text(self.USERNAME_REQUIRED)

    def erorinput_password(self):
        return self.get_text(self.PASSWORD_REQUIRED)
    