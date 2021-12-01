
from botdrivers.login import SetupDriver
from botdrivers.follow import FollowDriver
from repository import settings


class IgBot:

    def __init__(self):
        settings.initialize()
        self.setup_driver = SetupDriver(settings.username, settings.password)

    def login(self):
        self.setup_driver.start()

    @staticmethod
    def follow(account: str, limit: int):
        follow_driver = FollowDriver(account, limit)
        follow_driver.start()

    @staticmethod
    def unfollow(limit: int):
        unfollow_driver = FollowDriver(settings.username, limit, unfollow=True)
        unfollow_driver.start()

    def quit(self):
        self.setup_driver.quit()


if __name__ == '__main__':
    bot = IgBot()
    bot.login()
    bot.unfollow(10)
    bot.quit()
