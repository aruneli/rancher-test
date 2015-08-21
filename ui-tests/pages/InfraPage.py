__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from pages import BasePage
from locators import InfraPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfraPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_add_host(self):
        element = self.driver.find_element(*InfraPageLocators.InfraPageLocators.ADD_HOST_BUTTON)
        element.click()

    def get_add_host_hdr(self):
        element = self.driver.find_element(*InfraPageLocators.InfraPageLocators.ADD_HOST_HDR)
        return element.text


        #WebDriverWait(self.driver, 10).until(
         #   EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h2')))
        #WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element.)

