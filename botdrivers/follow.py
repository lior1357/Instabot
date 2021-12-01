from typing import List
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from .instadriver import IActionDriver
from repository import settings


class FollowDriver(IActionDriver):
    def __init__(self, account: str, limit: int, unfollow=False):
        super(FollowDriver, self).__init__()
        self.limit = limit
        self.account_url = settings.target_url + account
        self.unfollow = unfollow

        if unfollow:
            self.account_list = 'following'
            self.button_class = settings.unfollow_button_class

        else:
            self.account_list = 'followers'
            self.button_class = settings.follow_button_class

    def start(self):
        self.__get_accounts(self.account_list)
        followers = self.__scroll_for_followers()
        self.__click(followers)

    def __get_accounts(self, account_list: str):
        self.driver.get_url(self.account_url)
        # click followers link
        self.driver.locate_element_by_xpath_contains_formatted('a', 'href', account_list).click()

    def __scroll_for_followers(self):
        # locate scrollable element
        element = self.driver.locate_element_by_xpath_contains_formatted('div', 'class', 'isgrP')
        followers = self.__get_buttons_for_action(self.button_class)

        while len(followers) < self.limit:
            sleep(2)
            self.driver.scroll_element(element)
            followers = self.__get_buttons_for_action(self.button_class)

        return followers

    def __get_buttons_for_action(self, buttons_class: str):
        return self.driver.get_elements('button', 'class', buttons_class)

    def __click(self, accounts: List[WebElement]):
        if self.unfollow:
            for i in range(1, self.limit):
                accounts[i].click()
                self.driver.locate_element_by_text('button', 'Unfollow').click()
                sleep(10)
        else:
            for i in range(self.limit):
                accounts[i].click()
                sleep(10)
