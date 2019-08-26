

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login_admin(self, username, password):
        wd = self.app.wd
        self.app.open_admin()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()
