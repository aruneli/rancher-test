__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By

class Ec2Locators(object):
    ACCESS_KEY_INPUT = (By.ID, 'accessKey')
    SECRET_KEY_INPUT = (By.ID, 'secretKey')
    NEXT_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary")
    AVAILABILITY_ZONE = (By.XPATH, "//section[3]/div/div/span")
    ZONE_SELECT = (By.ID, "selectedZone")
    VPC_RADIO_BTN = (By.XPATH, "//div[3]/div[2]/div/label")
    SUBNET_RADIO_BTN = (By.XPATH, "//div[2]/label")
    SECURITY_GROUP = (By.XPATH, "///section[5]/div/div/span")
    INSTANCE = (By.XPATH, "//section[7]/div/div/span")
    ACCOUNT_ACCESS = (By.XPATH, "//section/div/div/span")
    STD_RADIO_BTN=(By.XPATH,"//section[5]/div[1]/div[2]/div[2]/div[1]/label/input")
    CUSTOM_RADIO_BTN=(By.XPATH,"//section[5]/div[1]/div[2]/div[2]/div[2]/label/input")
    SET_INSTANCE_OPTION_BTN = (By.XPATH, "//div[2]/button")
    SLIDE_BAR_CLICK_3 = (By.XPATH, "//div[2]/div[3]/div")
    HOST_NAME_INPUT = (By.ID, "prefix")
    HOST_DESC_INPUT = (By.ID, "description")
    HOST_INSTANCE_TYPE_SELECT = (By.ID, "instanceType")
    HOST_MEM_SIZE_INPUT = (By.ID, "rootSize")
    HOST_CREATE_BTN = (By.XPATH, "//div[2]/button")

    CREATING_HOST_PREFIX= "//section[2]/div["
    CREATING_HOST_SUFFIX= "]/div/div[1]/div[4]/a"

    STATUS_LABEL_PREFIX = "//section[2]/div["
    STATUS_LABEL_SUFFIX = "]/div/div[1]/div[2]/span"

    CLICK_MENU = (By.CSS_SELECTOR, "button.btn-circle-menu.dropdown-toggle")
    DEACTIVATE_LINK = (By.LINK_TEXT, 'Deactivate')
    DELETE_LINK = (By.LINK_TEXT, 'Delete')
    PURGE_LINK = (By.LINK_TEXT, "Purge")
    DELETE_BTN = (By.CSS_SELECTOR, 'button.btn.btn-danger')
    STATUS_TEXT = (By.XPATH, '//div[2]/div/div/div[2]/span')
    NO_HOST_FOUND_TEXT = (By.CSS_SELECTOR, 'div.text-center.text-muted')
