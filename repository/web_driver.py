from selenium import webdriver
from selenium.webdriver.common.by import By
from repository import settings
from auth.cookie_storage import CookieStorage
from .singleton import Singleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.common.exceptions import InvalidArgumentException


class SeleniumWebDriver(metaclass=Singleton):
    def __init__(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions())
        self.timeout = 10

    def get_url(self, url: str):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def add_cookies(self):
        cookie_storage = CookieStorage()

        for cookie in cookie_storage.cookies:
            self.driver.add_cookie(cookie)

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        CookieStorage.save_cookies(cookies=cookies)

    def locate_element_by_text(self, html_element, unique_value):
        element = WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located((By.XPATH, '//{}[contains(text(), "{}")]'.format(html_element, unique_value))))
        return element

    def locate_element_by_xpath_contains_formatted(self, html_element, css_field, unique_value, elements=False):
        xpath_format = '//{}[contains(@{}, "{}")]'
        element = WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located((By.XPATH, xpath_format.format(html_element, css_field, unique_value))))

        if elements is True:
            return element.find_elements_by_xpath("./child::*")

        return element

    def locate_element_by_xpath_formatted(self, html_element, css_field, unique_value, elements=False):
        xpath_format = '//{}[@{}="{}"]'
        element = WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located((By.XPATH, xpath_format.format(html_element, css_field, unique_value))))

        if elements is True:
            return element.find_elements_by_xpath("./child::*")

        return element

    def get_elements(self, html_element, css_field, unique_value):
        return self.driver.find_elements_by_xpath('//{}[contains(@{}, "{}")]'.format(html_element, css_field, unique_value))

    def find_element_by_xpath(self, xpath, elements=False):
        if elements is True:
            element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located((By.XPATH, xpath)))
            return element

    def focus_on_popup(self):
        """
        requested_window = None
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                requested_window = handle
                break
        try:
            self.driver.switch_to.window(requested_window)
        except InvalidArgumentException as e:
            print(str(e))
            print(self.driver.window_handles)
            print('no windows found except for main window')
"""
        sleep(5)
        print(self.driver.window_handles)

    @staticmethod
    def send_input_to_element(input_element, msg):
        input_element.clear()
        input_element.send_keys(msg)

    def get_page_html(self):
        return self.driver.page_source

    def scroll_element(self, element):
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', element)

    def close_all(self):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()

