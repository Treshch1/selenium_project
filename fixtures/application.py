from selenium import webdriver
from fixtures.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_admin(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/")