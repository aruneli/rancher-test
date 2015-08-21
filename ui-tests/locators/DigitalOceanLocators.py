__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By


class DigitalOceanLocators(object):
    SELECT_QUANTITY = (By.CSS_SELECTOR, "div.slider-bar")
    SLIDE_BAR_CLICK_3 = (By.XPATH, "//div/div/div[3]/div")
    HOST_NAME_INPUT = (By.ID, "prefix")
    HOST_DESC_INPUT = (By.ID, "description")
    ACCESS_TOKEN_INPUT = (By.ID, 'accessToken')
    IMAGE_SELECT = (By.ID, "image")
    HOST_MEM_SIZE_SELECT = (By.ID, "size")
    HOST_REGION_SELECT = (By.ID, "region")
    HOST_CREATE_BTN = (By.XPATH, "//div[2]/button")

