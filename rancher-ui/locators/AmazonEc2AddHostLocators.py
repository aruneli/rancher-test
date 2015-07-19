__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By

class AmazonEc2AddHostLocators(object):
    ACCESS_KEY_INPUT = (By.ID, 'accessKey')
    SECRET_KEY_INPUT = (By.ID, 'secretKey')
    NEXT_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary")


