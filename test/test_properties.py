def test_countries_sorting(app):
    app.session.login_admin()
    app.open_admin_country_page()

    countries = []
    links_to_zones = []

    rows = app.wd.find_elements_by_css_selector("tr.row")
    for row in rows:
        row_cells = row.find_elements_by_css_selector("td")
        country_name = row_cells[4].text
        countries.append(country_name)
        if int(row_cells[5].text) > 0:
            link_to_zone = row_cells[4].find_element_by_css_selector('a').get_attribute("href")
            links_to_zones.append(link_to_zone)
    assert countries == sorted(countries)
    for link in links_to_zones:
        app.wd.get(link)
        zone_names = [i.text for i in app.wd.find_elements_by_xpath("//table[@id='table-zones']//tr/td[3]")[:-1]]
        assert zone_names == sorted(zone_names)


def test_zones_sorting(app):
    app.session.login_admin()
    app.open_admin_zones_page()

    zones_links = [i.get_attribute("href") for i in app.wd.find_elements_by_xpath("//tr[@class='row']/td[3]/a")]
    for link in zones_links:
        app.wd.get(link)
        zone_names = [i.text for i in app.wd.find_elements_by_css_selector("option:checked")[1::2]]
        assert zone_names == sorted(zone_names)


def test_property_info(app):
    app.open_main_site()
    main_property = app.get_property_info_main_page()
    app.open_first_campaign_property()
    detailed_property = app.get_property_info_property_page()
    assert main_property["name"] == detailed_property["name"]
    assert main_property["price"] == detailed_property["price"]
    assert main_property["campaign_price"] == detailed_property["campaign_price"]
    assert main_property["price_style"] ==  detailed_property["price_style"] == "line-through"
    assert main_property["campaign_price_tag"] == detailed_property["campaign_price_tag"] == "strong"
    assert main_property["price_size"] < main_property["campaign_price_size"]
    assert detailed_property["price_size"] < detailed_property["campaign_price_size"]

    assert main_property["price_color"][0] == main_property["price_color"][1] == main_property["price_color"][2]
    assert main_property["campaign_price_color"][1] == main_property["campaign_price_color"][2] == 0

    assert detailed_property["price_color"][0] == detailed_property["price_color"][1]\
           == detailed_property["price_color"][2]
    assert detailed_property["campaign_price_color"][1] == detailed_property["campaign_price_color"][2] == 0
