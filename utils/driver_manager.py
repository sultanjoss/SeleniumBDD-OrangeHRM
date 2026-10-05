from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
from utils.logger_utils import LoggerUtils

class DriverManager:
    
    logger = LoggerUtils.get_logger("DriverManager")

    def __init__(self):
        self.driver = None

    def start_driver(self):
        self.logger.info("Starting browser")
        options = Options()

        if ConfigReader.is_headless():
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(
            options=options
        )

        if not ConfigReader.is_headless():
            self.driver.maximize_window()

        return self.driver
    
    def quit_driver(self):
        if self.driver:
            self.logger.info("Closing browser")
            self.driver.quit()

    
