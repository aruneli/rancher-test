__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import DigitalOceanLocators
from selenium.webdriver.support.ui import Select


class DigitalOcean(object):

    def __init__(self, driver):
        self.driver = driver

    def input_access_token(self, val):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.ACCESS_TOKEN_INPUT)
        element.clear()
        element.send_keys(val)

    def input_host_name(self,val):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.HOST_NAME_INPUT)
        element.clear()
        element.send_keys(val)

    def input_host_desc(self,val):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.HOST_DESC_INPUT)
        element.clear()
        element.send_keys(val)

    def select_quantity(self):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.SELECT_QUANTITY)
        return element.text

    def click_slide_bar(self):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.SLIDE_BAR_CLICK_3)
        element.click()

    def select_image(self, image):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.IMAGE_SELECT)
        select = Select(element)
        select.select_by_visible_text(image)

    def select_host_mem_size(self, mem_size):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.HOST_MEM_SIZE_SELECT)
        select = Select(element)
        select.select_by_visible_text(mem_size)

    def select_region(self, region):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.HOST_REGION_SELECT)
        select = Select(element)
        select.select_by_visible_text(region)

    def click_create_btn(self):
        element = self.driver.find_element(*DigitalOceanLocators.DigitalOceanLocators.HOST_CREATE_BTN)
        element.click()






