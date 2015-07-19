__author__ = 'aruneli'

from locators import AmazonEc2AddHostLocators


class AmazonEc2AddHost(object):
    def __init__(self, driver):
        self.driver = driver

    def type_access_key(self, val):
        element = self.driver.find_element(*AmazonEc2AddHostLocators.AmazonEc2AddHostLocators.ACCESS_KEY_INPUT)
        element.clear()
        element.send_keys(val)

    def type_secret_key(self,val):
        element = self.driver.find_element(*AmazonEc2AddHostLocators.AmazonEc2AddHostLocators.SECRET_KEY_INPUT)
        element.clear()
        element.send_keys(val)

    def click_next_btn(self):
        element = self.driver.find_element(*AmazonEc2AddHostLocators.AmazonEc2AddHostLocators.NEXT_BTN)
        element.click()
