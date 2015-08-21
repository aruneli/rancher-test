__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By

class InfraPageLocators(object):
    ADD_HOST_BUTTON = (By.LINK_TEXT, 'Add Host')
    ADD_HOST_HDR = (By.CSS_SELECTOR, "h2")
    EC2_IMG = (By.XPATH, "//div[2]/ul/li/a")

