__author__ = 'aruneli'


from selenium.webdriver.common.by import By

class WelcomePageLocators(object):
    RANCHER_ICON = (By.CSS_SELECTOR, 'div.logo')
    INFRA_TAB = (By.LINK_TEXT, 'INFRASTRUCTURE')
    APP_TAB = (By.LINK_TEXT, 'APPLICATIONS')


