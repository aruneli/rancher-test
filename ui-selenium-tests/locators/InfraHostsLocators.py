__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium.webdriver.common.by import By


class InfraHostsLocators(object):

    STATUS_LABEL = "/html/body/div/div[6]/div/main/section[2]/div[1]/div/div[1]/div[2]/span"
    CREATING_HOST_PREFIX= "//section[2]/div["
    CREATING_HOST_SUFFIX= "]/div/div[1]/div[2]/span"
    STATUS_LABEL_PREFIX = "//section[2]/div["
    STATUS_LABEL_SUFFIX = "]/div/div[1]/div[2]/span"
    CLICK_MENU = (By.CSS_SELECTOR, "button.btn-circle-menu.dropdown-toggle")
    DEACTIVATE_LINK = (By.LINK_TEXT, 'Deactivate')
    DELETE_LINK = (By.LINK_TEXT, 'Delete')
    PURGE_LINK = (By.LINK_TEXT, "Purge")
    DELETE_BTN = (By.CSS_SELECTOR, 'button.btn.btn-danger')
    STATUS_TEXT = (By.XPATH, '//div[2]/div/div/div[2]/span')
    NO_HOST_FOUND_TEXT = (By.CSS_SELECTOR, 'div.text-center.text-muted')

