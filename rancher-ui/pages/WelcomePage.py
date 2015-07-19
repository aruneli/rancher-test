from pages import BasePage
from locators import WelcomePageLocators

class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        return "Rancher" in self.driver.title

    def click_infra_tab(self):
        element = self.driver.find_element(*WelcomePageLocators.WelcomePageLocators.INFRA_TAB)
        element.click()

    def click_app_tab(self):
        element = self.driver.find_element(*WelcomePageLocators.WelcomePageLocators.APP_TAB)
        element.click()

    def click_rancher_about(self):
        element = self.driver.find_element(*WelcomePageLocators.WelcomePageLocators.RANCHER_ICON)
        element.click()

