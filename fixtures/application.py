from selenium import webdriver
from fixtures.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_admin(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/")

    def open_main_site(self):
        wd = self.wd
        wd.get("http://localhost/litecart/")
