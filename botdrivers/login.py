from .instadriver import IActionDriver
from selenium.webdriver.common.keys import Keys
from repository import settings


class SetupDriver(IActionDriver):
    def __init__(self, username: str, password: str):
        super(SetupDriver, self).__init__()
        self.username = username
        self.password = password

    def start(self):
        if self.__is_not_logged_in():
            self.__login_manually()
        else:
            self.__login_with_cookies()

        self.__discard_notice()

    def __login_with_cookies(self):
        self.driver.get_url(settings.target_url)
        self.driver.add_cookies()
        self.driver.refresh()

    def __login_manually(self):
        username_input = self.driver.locate_element_by_xpath_formatted('input', 'name', 'username')
        self.driver.send_input_to_element(username_input, self.username)

        password_input = self.driver.locate_element_by_xpath_formatted('input', 'name', 'password')
        self.driver.send_input_to_element(username_input, self.password)

        password_input.send_keys(Keys.RETURN)

    def __is_not_logged_in(self):
        html_page = self.driver.get_page_html()
        return settings.login_page_unique_string in html_page

    def __discard_notice(self):
        self.driver.locate_element_by_text('button', "Not Now").click()

    def quit(self):
        self.driver.save_cookies()
        self.driver.close_all()
