from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Wait:
    def __init__(self, function):
        self.function = function

    def __call__(self, web_driver):
        def decorator(function):
            def wrapper(*args):
                element = WebDriverWait(web_driver, 10).until(ec.presence_of_element_located(
                    function(*args)
                ))
                return element

            return wrapper
        return decorator
