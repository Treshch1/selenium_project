from selenium import webdriver
from selenium.webdriver.support.color import Color
from fixtures.session import SessionHelper
from fixtures.registration import RegistrationHelper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path


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

    def open_add_new_catalog_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//span[@class='name' and .='Catalog']").click()
        wd.find_element_by_xpath("//a[@class='button' and .=' Add New Product']").click()

    def upload_image(self):
        wd = self.wd
        input_image_element = wd.find_element_by_name("new_images[]")
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inner_yard.jpg")
        input_image_element.send_keys(file_path)

    def get_cart_quntity(self):
        wd = self.wd
        return int(wd.find_element_by_css_selector('span.quantity').text)

    def add_item_to_the_cart(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@title='New']").click()
        wd.find_element_by_name("add_cart_product").click()
        WebDriverWait(wd, 3).until(EC.alert_is_present())
        alert = wd.switch_to.alert
        alert.accept()
        self.open_main_site()

    def open_cart(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[.='Checkout »']").click()

    def is_image_displayed(self):
        wd = self.wd
        return wd.find_elements_by_css_selector("td.content img")

    def remove_item_from_cart(self):
        wd = self.wd
        wd.find_element_by_name("remove_cart_item").click()

    def get_table_element(self):
        wd = self.wd
        return wd.find_element_by_css_selector("table.dataTable")

    def wait_until_element_become_changed(self, element):
        wd = self.wd
        WebDriverWait(wd, 10).until(EC.staleness_of(element))

    def open_add_new_country(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[.= ' Add New Country']").click()

    def get_all_external_links(self):
        wd = self.wd
        return wd.find_elements_by_css_selector("i.fa.fa-external-link")

    def wait_new_window_and_close(self, element):
        wd = self.wd
        current_handle = wd.current_window_handle
        # yield
        element.click()
        WebDriverWait(wd, 10).until(
            lambda wd: 1 != len(wd.window_handles))
        for i in wd.window_handles:
            if i != current_handle:
                new_handle = i
                break
        wd.switch_to.window(new_handle)
        wd.close()
        wd.switch_to.window(current_handle)
