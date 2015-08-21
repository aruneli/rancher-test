__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By


class AppsLocators(object):

    ADD_SERVICE_BUTTON = (By.LINK_TEXT, 'Add Service')
    SERVICE_NAME_INPUT = (By.ID, "name")
    SERVICE_DESCRIPTION_INPUT = (By.ID, "description")
    SLIDE_BAR_CLICK_3 = (By.XPATH, "//div[3]/div/div[2]")
    SERVICE_IMAGE_INPUT = (By.ID, "userImageUuid")
    SERVICE_CREATE_BTN = (By.XPATH, "//div[4]/button")





