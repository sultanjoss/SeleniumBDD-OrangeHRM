from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader
from selenium.common.exceptions import TimeoutException
from utils.logger_utils import LoggerUtils

class BasePage:

    logger = LoggerUtils.get_logger("BasePage")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,
        ConfigReader.get_explicit_wait())

    def open_url(self,url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self,locator):
        self.logger.info(f"Clicking element: {locator}")
        self.find(locator).click()

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator}")
        self.find(locator).send_keys(text)

    def get_text(self,locator):
        return self.find(locator).text

    def is_visible(self,locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True

        except TimeoutException:
            return False
