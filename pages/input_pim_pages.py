from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pathlib import Path


class InputPIMpage(BasePage):

    PIM_Menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']/span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
    EMPLOYEE_INFROMATION_TITLE = (By.XPATH, "//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title']")
    EMPLOYEE_INPUT_NAMA = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[1]//input[1]")
    EMPLOYEE_INPUT_ID = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//input[@class='oxd-input oxd-input--active']")
    EMPLOYEE_STATUS_DROPDOWN = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[3]//div[@class='oxd-select-text oxd-select-text--active']")
    INCLUDE_DROPDOWN = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[@class='oxd-select-text oxd-select-text--active']/div[.='Current Employees Only']")
    SUPERVISOR_NAME = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[5]//input[1]")
    JOB_TITLE_DROPDOWN = (By.XPATH,"//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[6]//div[@class='oxd-select-text oxd-select-text--active']")
    SUB_UNIT_DROPDOWN = (By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']/div[7]//div[@class='oxd-select-text oxd-select-text--active']")
    SEARCH_BUTTON = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    HASIL_PENCARIAN = (By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']")

    def open_pim_menu(self):
        self.click(self.PIM_Menu)

    def employee_information_displayed(self):
        return self.is_visible(self.EMPLOYEE_INFROMATION_TITLE)

    def input_employee_name(self, employee_name):
        self.select_autocomplete(self.EMPLOYEE_INPUT_NAMA, employee_name)

    def input_employee_id(self,employee_id):
        self.type(self.EMPLOYEE_INPUT_ID, employee_id)

    def input_supervisor_name(self, supervisor_name):
        self.select_autocomplete(self.SUPERVISOR_NAME, supervisor_name)

    def click_button_search(self):
        self.click(self.SEARCH_BUTTON)

    def select_dropdown(self, dropdown_locator, option_text): # << untuk dropdown custom (Mesinnya)
        self.click(dropdown_locator)
        option_locator = (
        By.XPATH,
        f"//div[@role='option']//span[normalize-space()='{option_text}']")
        self.click(option_locator)

    def pilih_employee_status(self,status):
        self.select_dropdown(self.EMPLOYEE_STATUS_DROPDOWN, status)

    def pilih_include(self, include):
        self.select_dropdown(self.INCLUDE_DROPDOWN, include)

    def pilih_job_title(self, title):
        self.select_dropdown(self.JOB_TITLE_DROPDOWN,title)

    def pilih_sub_unit(self, sub_unit):
        self.select_dropdown(self.SUB_UNIT_DROPDOWN, sub_unit)


    def select_autocomplete(self, input_locator, keyword): # untuk modelan pencarian saat di click/input muncul pilihan untuk mencari tulisan tersebut

        self.type(input_locator,keyword)
        option_locator = (By.XPATH,"//div[@role='option']//span")
        self.click(option_locator)

    def get_record_found(self):
        return self.find(self.HASIL_PENCARIAN).is_displayed()


    #-----------ADD Employe-------------#

#-----LOCATOR

    ADD_EMPLOYEE_BUTTON = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    DASHBOARD_ADD_EMPLOYEE = (By.XPATH,"//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']")
    INPUT_FIRST_NAME = (By.XPATH,"//input[@name='firstName']")
    INPUT_MIDDLE_NAME = (By.XPATH,"//input[@name='middleName']")
    INPUT_LAST_NAME = (By.XPATH,"//input[@name='lastName']")
    INPUT_PEKERJA_ID = (By.XPATH,"//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input[@class='oxd-input oxd-input--active']")
    TOMBOL_SAVE = (By.XPATH,"//button[@type='submit' and normalize-space()='Save']")
    ADD_FOTO = (By.XPATH,"//input[@type='file']")
    HALAMAN_PERSONAL_DETAILS = (By.XPATH,"//h6[.='Personal Details']")

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def tampilan_add_employee(self):
        return self.find(self.DASHBOARD_ADD_EMPLOYEE).is_displayed()

    def masukkan_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)

    def masukkan_middle_name(self, middle_name):
        self.type(self.INPUT_MIDDLE_NAME, middle_name)

    def masukkan_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def masukkan_pekerja_ID(self, pekerja_id):
        element = self.find(self.INPUT_PEKERJA_ID)
        element.clear()
        element.send_keys(pekerja_id)

    def click_tombol_save(self):
        self.click(self.TOMBOL_SAVE)

    def upload_profile_photo(self, photo_path):
        project_root = Path(__file__).resolve().parent.parent
        absolute_path = (project_root / photo_path).resolve()

        file_input = self.driver.find_element(*self.ADD_FOTO)
        file_input.send_keys(str(absolute_path))

    def halaman_personal_details(self):
        return self.find(self.HALAMAN_PERSONAL_DETAILS).is_displayed()
    




