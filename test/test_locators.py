import time

def test_titles_in_admin(app):
    app.session.login_admin("admin", "admin")
    all_tabs = app.wd.find_elements_by_id("app-")
    for tab_index in range(len(all_tabs)):
        needed_tab = app.wd.find_elements_by_id("app-")[tab_index]
        needed_tab.click()
        all_sub_tabs = app.wd.find_elements_by_xpath("//li[@id='app-']//li")
        if len(all_sub_tabs) > 0:
            for sub_tab_index in range(len(all_sub_tabs)):
                needed_sub_tab = app.wd.find_elements_by_xpath("//li[@id='app-']//li")[sub_tab_index]
                needed_sub_tab.click()
                title = app.wd.find_element_by_tag_name("h1")
                assert title.is_displayed()
        else:
            title = app.wd.find_element_by_tag_name("h1")
            assert title.is_displayed()

def test_lables_on_landing_page(app):
    app.open_main_site()
    all_products = app.wd.find_elements_by_css_selector("li.product")
    for product in all_products:
        stickers = product.find_elements_by_css_selector("div.sticker")
        assert len(stickers) == 1
