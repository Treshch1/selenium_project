import random
import string


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def test_registration(app):
    app.open_main_site()
    app.registration.open_create_account_page()
    email = random_string(10) + "@gmail.com"
    password = "qqweqqwe"
    app.registration.fill_registration_form(email, password)
    app.registration.submit_registration_form()
    app.registration.fill_password(password)
    app.registration.submit_registration_form()
    app.registration.logout()
    app.registration.open_login_form()
    app.registration.fill_login_form(email, password)
    app.registration.submit_login_form()
    app.registration.logout()


def test_image_uploading(app):
    app.session.login_admin()
    app.open_add_new_catalog_page()
    app.upload_image()
