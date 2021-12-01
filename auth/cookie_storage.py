import pickle
from repository import settings


class CookieStorage:
    def __init__(self):
        cookies = pickle.load(open(settings.cookie_file_path, "rb"))
        self.cookies = cookies

    @staticmethod
    def save_cookies(cookies):
        pickle.dump(cookies, open(settings.cookie_file_path, "wb"))
