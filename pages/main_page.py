import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

class Main_page(Base):
    url = 'https://demoqa.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    elements_btn = "//h5[text()='Elements']"

    # Getters
    def get_elements_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.elements_btn)))

    # Actions
    def scroll_main_page(self):
        self.driver.execute_script('window.scrollTo(0,150)')
        print('Scroll to elements btn')

    def click_elements_btn(self):
        self.get_elements_btn().click()
        print('Click Elements btn')

    # Methods

    def elements_btns(self):
        with allure.step("Click elements button"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.scroll_main_page()
            self.click_elements_btn()
