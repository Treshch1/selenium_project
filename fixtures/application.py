from selenium import webdriver
from selenium.webdriver.support.color import Color
from fixtures.session import SessionHelper
from fixtures.registration import RegistrationHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.registration = RegistrationHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_admin(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/")

    def open_main_site(self):
        wd = self.wd
        wd.get("http://localhost/litecart/")

    def open_admin_country_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    def open_admin_zones_page(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    def get_property_info_main_page(self):
        property_element = self.wd.find_element_by_css_selector("div#box-campaigns li.product")
        property_name = property_element.find_element_by_css_selector("div.name").text
        property_price = property_element.find_element_by_css_selector("s.regular-price")
        property_price_text = property_price.text
        property_price_size = property_price.size
        property_price_color = property_price.value_of_css_property("color")
        property_price_color_values = [self.get_red_value(property_price_color),
                                       self.get_green_value(property_price_color),
                                       self.get_blue_value(property_price_color)]
        property_price_style = property_price.value_of_css_property("text-decoration-line")
        campaign_price = property_element.find_element_by_css_selector("strong.campaign-price")
        campaign_price_color = campaign_price.value_of_css_property("color")
        campaign_price_color_values = [self.get_red_value(campaign_price_color),
                                       self.get_green_value(campaign_price_color),
                                       self.get_blue_value(campaign_price_color)]
        campaign_price_tag = campaign_price.tag_name
        campaign_price_size = campaign_price.size
        campaign_price_text = campaign_price.text
        property_info = {"name": property_name, "price": property_price_text,
                         "price_size": property_price_size["height"] * property_price_size["width"],
                         "price_color": property_price_color_values, "price_style": property_price_style,
                         "campaign_price": campaign_price_text, "campaign_price_color": campaign_price_color_values,
                         "campaign_price_tag": campaign_price_tag,
                         "campaign_price_size": campaign_price_size["height"] * campaign_price_size["width"]}
        return property_info

    def get_property_info_property_page(self):
        property_name = self.wd.find_element_by_css_selector("h1.title").text
        property_price = self.wd.find_element_by_css_selector("s.regular-price")
        property_price_text = property_price.text
        property_price_size = property_price.size
        property_price_color = property_price.value_of_css_property("color")
        property_price_color_values = [self.get_red_value(property_price_color),
                                       self.get_green_value(property_price_color),
                                       self.get_blue_value(property_price_color)]
        property_price_style = property_price.value_of_css_property("text-decoration-line")
        campaign_price = self.wd.find_element_by_css_selector("strong.campaign-price")
        campaign_price_color = campaign_price.value_of_css_property("color")
        campaign_price_color_values = [self.get_red_value(campaign_price_color),
                                       self.get_green_value(campaign_price_color),
                                       self.get_blue_value(campaign_price_color)]
        campaign_price_tag = campaign_price.tag_name
        campaign_price_size = campaign_price.size
        campaign_price_text = campaign_price.text
        property_info = {"name": property_name, "price": property_price_text,
                         "price_size": property_price_size["height"] * property_price_size["width"],
                         "price_color": property_price_color_values, "price_style": property_price_style,
                         "campaign_price": campaign_price_text, "campaign_price_color": campaign_price_color_values,
                         "campaign_price_tag": campaign_price_tag,
                         "campaign_price_size": campaign_price_size["height"] * campaign_price_size["width"]}
        return property_info

    def open_first_campaign_property(self):
        self.wd.find_element_by_css_selector("div#box-campaigns li.product").click()

    def get_red_value(self, color):
        return Color.from_string(color).red

    def get_blue_value(self, color):
        return Color.from_string(color).blue

    def get_green_value(self, color):
        return Color.from_string(color).green

