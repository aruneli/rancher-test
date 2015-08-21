__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import HostRegistrationLocators
from selenium.webdriver.support.ui import Select


class HostRegistration (object):

    def __init__(self, driver):
        self.driver = driver

    def get_access_control_txt(self):
        element = self.driver.find_element(*HostRegistrationLocators.HostRegistrationLocators.ACCESS_CONTROL_TEXT)
        return element.text

    def get_host_registration_txt(self):
        element = self.driver.find_element(*HostRegistrationLocators.HostRegistrationLocators.HOST_REGISTRATION_HDR)
        return element.text

    def click_save_btn(self):
        element = self.driver.find_element(*HostRegistrationLocators.HostRegistrationLocators.SAVE_BTN)
        element.click()





