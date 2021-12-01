from abc import abstractmethod, ABC
from repository.web_driver import SeleniumWebDriver


class IActionDriver(ABC):
    @abstractmethod
    def __init__(self):
        self.driver = SeleniumWebDriver()

    @abstractmethod
    def start(self):
        return

"""
    @classmethod
    def __subclasshook__(cls, instance):
        required = ["start"]
        return_value = True
        for r in required:
            if not any(r in c.__dict__ for c in instance.__mro__):
                return_value = NotImplemented
        return return_value
"""