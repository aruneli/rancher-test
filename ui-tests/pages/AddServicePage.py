__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import AppsLocators
from selenium.webdriver.support.ui import Select


class AddService(object):

    def __init__(self, driver):
        self.driver = driver

    def click_add_service(self):
        element = self.driver.find_element(*AppsLocators.AppsLocators.ADD_SERVICE_BUTTON)
        element.click()

    def input_service_name(self, val):
        element = self.driver.find_element(*AppsLocators.AppsLocators.SERVICE_NAME_INPUT)
        element.clear()
        element.send_keys(val)

    def input_service_description(self, val):
        element = self.driver.find_element(*AppsLocators.AppsLocators.SERVICE_DESCRIPTION_INPUT)
        element.clear()
        element.send_keys(val)

    def click_slide_bar_3(self):
        element = self.driver.find_element(*AppsLocators.AppsLocators.SLIDE_BAR_CLICK_3)
        element.click()

    def input_image_name(self, val):
        element = self.driver.find_element(*AppsLocators.AppsLocators.SERVICE_IMAGE_INPUT)
        element.clear()
        element.send_keys(val)

    def click_create_btn(self):
        element = self.driver.find_element(*AppsLocators.AppsLocators.SERVICE_CREATE_BTN)
        element.click()






