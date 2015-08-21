__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By

class HostRegistrationLocators(object):
    ACCESS_CONTROL_TEXT = (By.CSS_SELECTOR, 'article.warning')
    HOST_REGISTRATION_HDR = (By.CSS_SELECTOR, 'section.header > h3')
    SAVE_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary")


