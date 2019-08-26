from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_admin(self):
        wd = self.app.wd
        self.app.open_admin()
        try:
            wd.find_element_by_name("username").send_keys("admin")
            wd.find_element_by_name("password").send_keys("admin")
            wd.find_element_by_name("login").click()
        except NoSuchElementException:
            pass
