__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By

class DigitalOceanLocators(object):
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

