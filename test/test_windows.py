def test_new_tab_opening(app):
    app.open_admin()
    app.session.login_admin()
    app.open_admin_country_page()
    app.open_add_new_country()
    for external_link in app.get_all_external_links():
        app.wait_new_window_and_close(external_link)
