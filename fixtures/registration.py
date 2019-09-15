from selenium.webdriver.support.ui import Select


class RegistrationHelper:

    def __init__(self, app):
        self.app = app

    def open_create_account_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[.='Create Account']").click()

    def fill_registration_form(self, email, password):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys("q")
        wd.find_element_by_name("lastname").send_keys("q")
        wd.find_element_by_name("address1").send_keys("q")
        wd.find_element_by_name("postcode").send_keys("11111")
        wd.find_element_by_name("city").send_keys("q")
        country = Select(wd.find_element_by_name("country_code"))
        country.select_by_visible_text("United States")
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("phone").send_keys("1")
        self.fill_password(password)

    def submit_registration_form(self):
        wd = self.app.wd
        wd.find_element_by_name("create_account").click()

    def fill_password(self, password):
        wd = self.app.wd
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("confirmed_password").send_keys(password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[.='Logout']").click()

    def open_login_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[.='Login']").click()

    def fill_login_form(self, email, password):
        wd = self.app.wd
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("password").send_keys(password)

    def submit_login_form(self):
        wd = self.app.wd
        wd.find_element_by_name("login").click()
