__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import InfraHostsLocators
from locators import InfraPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time


class InfraHostsPage(object):

    NO_HOST_TEXT = "No hosts or containers yet."
    MAX_WAIT_TIME = 600
    STATUS_BOOTSTRAPPING = "BOOTSTRAPPING"
    STATUS_CREATING = "CREATING"
    STATUS_ERROR = "ERROR"
    STATUS_ACTIVE = "ACTIVE"
    STATUS_INACTIVE = "INACTIVE"
    STATUS_REMOVED = "REMOVED"

    def __init__(self, driver):
        self.driver = driver


    def click_ec2_img(self):
        element = self.driver.find_element(*InfraPageLocators.InfraPageLocators.EC2_IMG)
        element.click()

    def get_host_status_text(self):
        xpath_loc = InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_PREFIX + "1" + InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_SUFFIX
        print xpath_loc
        by = (By.XPATH, xpath_loc)
        element = self.driver.find_element(*by)
        return element.text

    def get_host_status_element(self):
        xpath_loc = InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_PREFIX + "1" + InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_SUFFIX
        print xpath_loc
        by = (By.XPATH, xpath_loc)
        element = self.driver.find_element(*by)
        return element

    def check_creating_host(self, num_host):
        for x in range(1, num_host):
            xpath_loc = InfraHostsLocators.InfraHostsLocators.CREATING_HOST_PREFIX + str(
                x) + InfraHostsLocators.InfraHostsLocators.CREATING_HOST_SUFFIX
            print xpath_loc
            by = (By.XPATH, xpath_loc)
            element = self.driver.find_element(*by)
            cur_txt = element.text
            assert cur_txt, "CREATING"

    def wait_for_first_host_active(self, value):
        xpath_loc = InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_PREFIX + "1" + InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_SUFFIX
        print xpath_loc
        by = (By.XPATH, xpath_loc)
        element = self.driver.find_element(*by)
        element = WebDriverWait(self.driver, 180).until(ec.text_to_be_present_in_element_value(element, value))

    # def wait_for_other_hosts_active(self, num_host, status):
    #     is_all_active = False
    #     sec = 0
    #     max_wait_time = 120
    #     while is_all_active:
    #         for x in range(1,num_host):
    #             xpath_loc = InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_PREFIX + x + InfraHostsLocators.InfraHostsLocators.STATUS_LABEL_SUFFIX
    #             print xpath_loc
    #             element = self.driver.find_element(xpath_loc)
    #             cur_txt = element.text
    #             try:
    #                 assert cur_txt, status
    #                 is_cur_active = True
    #             except Exception as e:
    #                 print e.message
    #                 is_cur_active = False
    #
    #             if check_all_active(collection):
    #                 is_all_active = True
    #             else:
    #                 time.sleep(1)
    #                 sec += 1
    #
    #         if sec > max_wait_time:
    #             self.fail("time out")
    #             break

    def is_no_host_text_found(self):
        try:
            element = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.NO_HOST_FOUND_TEXT)
            element.is_displayed()
            print "No Host Found"
            return True
        except Exception as e:
            print "No Host not Found"
            return False

    def click_menu(self):
        status = self.get_host_status_element()
        hidden_menu = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.CLICK_MENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(status)
        actions.click(hidden_menu)
        actions.perform()

    def click_deactivate_link(self):
        element = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.DEACTIVATE_LINK)
        element.click()

    def click_delete_link(self):
        element = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.DELETE_LINK)
        element.click()

    def click_purge_link(self):
        element = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.PURGE_LINK)
        element.click()

    def click_delete_btn(self):
        element = self.driver.find_element(*InfraHostsLocators.InfraHostsLocators.DELETE_BTN)
        element.click()

    def _host_delete(self):
        print "Inside _host_delete"
        host_status = self.get_host_status_text()
        print host_status
        time.sleep(2)
        if host_status == self.STATUS_CREATING:
            self.click_menu()
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_BOOTSTRAPPING:
            self.click_menu()
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_ERROR:
            self.click_menu()
            time.sleep(2)
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_ACTIVE:
            self.click_menu()
            time.sleep(2)
            self.click_deactivate_link()
            time.sleep(2)
            self.click_menu()
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_INACTIVE:
            self.click_menu()
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_REMOVED:
            self.click_menu()
            self.click_purge_link()
            time.sleep(2)
        if host_status != self.STATUS_REMOVED:
            self.click_delete_btn()
            time.sleep(2)

    def host_delete(self):
        print "Inside host_delete"
        sec = 0
        is_no_host = self.is_no_host_text_found()
        print is_no_host
        while is_no_host is not True:
            print "Calling _host_delete"
            self._host_delete()
            time.sleep(2)
            print "end of host_delete"
            is_no_host = self.is_no_host_text_found()
            print "Host status now: %s" % is_no_host


