from selenium.webdriver.common.by import By

from pages.base_page import BasePage

#untuk ekspetasi user ini di gherkin THEN

class DashboardPage(BasePage):

    DASHBOARD_TITLE = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def memastikantulisan_dashboard(self):
        return self.find(self.DASHBOARD_TITLE)