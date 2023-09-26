import time
import allure
from lib2to3.pgen2 import driver
# from selenium import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Elements_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    textbox_btn = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]/span"
    full_name = "//input[@placeholder='Full Name']"
    email = "//input[@placeholder='name@example.com']"
    current_address = "//textarea[@placeholder='Current Address']"
    permanent_address = "//textarea[@id='permanentAddress']"
    submit_btn = "//button[@id='submit']"
    name_text = "//p[@id='name']"
    email_text = "//p[@id='email']"
    current_address_text = "//p[@id='currentAddress']"
    permanent_address_text = "//p[@id='permanentAddress']"

    buttons_btn = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[5]/span"
    click_me = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button"
    click_me_text = "//p[@id='dynamicClickMessage']"
    right_click_me = "//button[@id='rightClickBtn']"
    right_click_me_text = "//p[@id='rightClickMessage']"
    double_click_me = "//button[@id='doubleClickBtn']"
    double_click_me_text = "//p[@id='doubleClickMessage']"

    alerts_frame_windows = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/span/div/div[1]"
    browser_windows = "//span[text()='Browser Windows']"
    new_tab = "//button[@id ='tabButton']"
    new_window = "//button[@id='windowButton']"

    alerts = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/ul/li[2]/span"
    first_alert = "//button[@id='alertButton']"
    second_alert = "//button[@id='timerAlertButton']"
    third_alert = "//button[@id='confirmButton']"
    confirm_result = "//span[@id='confirmResult']"
    fourth_alert = "//button[@id='promtButton']"
    entered_result = "//span[@id='promptResult']"


    # Getters

    def get_textbox_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.textbox_btn)))

    def get_full_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_current_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.current_address)))

    def get_permanent_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.permanent_address)))

    def get_submit_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_btn)))

    def get_name_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name_text)))

    def get_email_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_text)))

    def get_current_address_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.current_address_text)))

    def get_permanent_address_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.permanent_address_text)))


    def get_buttons_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buttons_btn)))

    def get_click_me(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_me)))

    def get_click_me_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.click_me_text)))

    def get_right_click_me(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.right_click_me)))

    def get_right_click_me_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.right_click_me_text)))

    def get_double_click_me(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.double_click_me)))

    def get_double_click_me_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.double_click_me_text)))


    def get_alerts_frame_windows(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.alerts_frame_windows)))

    def get_browser_windows(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.browser_windows)))

    def get_new_tab(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.new_tab)))

    def get_new_window(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.new_window)))


    def get_alerts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.alerts)))

    def get_first_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_alert)))

    def get_second_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.second_alert)))

    def get_third_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.third_alert)))

    def get_confirm_result(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_result)))

    def get_fourth_alert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fourth_alert)))

    def get_entered_result(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.entered_result)))



    # Actions
    def click_textbox_btn(self):
        self.get_textbox_btn().click()
        print('Click text box btn')

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print('Input full name')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email')

    def input_current_address(self, current_address):
        self.get_current_address().send_keys(current_address)
        print('Input current address')

    def input_permanent_address(self, permanent_address):
        self.get_permanent_address().send_keys(permanent_address)
        print('Input permanent address')

    def scroll_elements_page(self):
        self.driver.execute_script('window.scrollTo(0,220)')
        print('Scroll to elements page')

    def click_submit_btn(self):
        self.get_submit_btn().click()
        print('Click submit btn')



    def click_buttons_btn(self):
        self.get_buttons_btn().click()
        print('Click Buttons bth')

    def click_click_me(self):
        self.get_click_me().click()
        print('Click me')

    def click_right_click_me(self):
        action = ActionChains(self.driver)
        action.context_click(self.get_right_click_me()).perform()
        print('Right click')

    def click_double_click_me(self):
        action = ActionChains(self.driver)
        action.double_click(self.get_double_click_me()).perform()
        print('Double click')

    def scroll_to_alerts_btn(self):
        self.driver.execute_script('window.scrollTo(0,1000)')
        print('Scroll to alerts btn')


    def click_alerts_frame_windows_btn(self):
        self.get_alerts_frame_windows().click()
        print('Click alerts frame windows')

    def click_browser_windows(self):
        self.get_browser_windows().click()
        print('Click browser windows')

    def click_new_tab(self):
        self.get_new_tab().click()
        print('Click new tab')
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def click_new_window(self):
        self.get_new_window().click()
        print('Click new window')
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(original_window)



    def scroll_to_alerts(self):  # for Alerts btn
        self.driver.execute_script('window.scrollTo(0,100)')
        print('Scroll to alerts_btn')

    def click_alerts_btn(self):
        self.get_alerts().click()
        print('Click alerts btn')
        time.sleep(3)

    def click_first_alert_btn(self):
        self.get_first_alert().click()
        print('Click first alert button')
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def click_second_alert_btn(self):
        self.get_second_alert().click()
        print('Click second alert button')
        time.sleep(6)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def click_third_alert_btn(self):
        self.get_third_alert().click()
        print('Click third alert button')
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        self.assert_word(self.get_confirm_result(), 'You selected Ok')
        time.sleep(2)

    def click_fourth_alert_btn(self):
        self.get_fourth_alert().click()
        print('Click fourth alert button')
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.send_keys('Test name')
        alert.accept()
        self.assert_word(self.get_entered_result(), 'You entered Test name')
        # time.sleep(2)



    # Methods
    def textbox_button (self):
        with allure.step("Textbox button"):
            self.click_textbox_btn()
            time.sleep(3)
            self.input_full_name('Иванов Иван Иванович')
            self.input_email('ex@gmail.com')
            self.input_current_address('Спб, Большая Зеленина, 16')
            self.input_permanent_address('Мск, Ленина, 12')
            self.scroll_elements_page()
            self.click_submit_btn()
            self.assert_word(self.get_name_text(), "Name:Иванов Иван Иванович")
            self.assert_word(self.get_email_text(), "Email:ex@gmail.com")
            self.assert_word(self.get_current_address_text(), "Current Address :Спб, Большая Зеленина, 16")
            self.assert_word(self.get_permanent_address_text(), "Permananet Address :Мск, Ленина, 12")

    def buttons_button(self):
        with allure.step("Buttons button"):
            self.click_buttons_btn()
            time.sleep(3)
            self.click_click_me()
            time.sleep(3)
            self.assert_word(self.get_click_me_text(), 'You have done a dynamic click')
            self.click_right_click_me()
            self.assert_word(self.get_right_click_me_text(), 'You have done a right click')
            self.click_double_click_me()
            self.assert_word(self.get_double_click_me_text(), 'You have done a double click')

    def alerts_frame_windows_btn(self):
        with allure.step("Alerts,Frame and windows button"):
            self.scroll_to_alerts_btn()
            time.sleep(2)
            self.click_alerts_frame_windows_btn()
            self.click_browser_windows()
            time.sleep(2)
            self.click_new_tab()
            self.click_new_window()

    def alerts_page(self):
        with allure.step("Alerts page"):
            self.scroll_to_alerts()
            self.click_alerts_btn()
            self.click_first_alert_btn()
            self.click_second_alert_btn()
            self.click_third_alert_btn()
            self.click_fourth_alert_btn()





