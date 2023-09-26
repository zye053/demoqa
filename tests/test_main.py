from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.elements_page import Elements_page
from pages.main_page import Main_page
import allure


@allure.description('Main page')
def test_main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print('Start test')

    main_page = Main_page(driver)
    main_page.elements_btns()

    el_page = Elements_page(driver)
    el_page.textbox_button()

    el_page = Elements_page(driver)
    el_page.buttons_button()

    el_page = Elements_page(driver)
    el_page.alerts_frame_windows_btn()

    el_page = Elements_page(driver)
    el_page.alerts_page()


