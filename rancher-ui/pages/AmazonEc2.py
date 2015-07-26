from selenium.webdriver import ActionChains

__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import AmazonEc2Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AmazonEc2(object):

    NO_HOST_TEXT = "No hosts or containers yet."
    MAX_WAIT_TIME = 60
    STATUS_ERROR = "ERROR"
    STATUS_ACTIVE = "ACTIVE"
    STATUS_INACTIVE ="INACTIVE"
    STATUS_REMOVED = "REMOVED"

    def __init__(self, driver):
        self.driver = driver

    def type_access_key(self, val):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.ACCESS_KEY_INPUT)
        element.clear()
        element.send_keys(val)

    def type_secret_key(self,val):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.SECRET_KEY_INPUT)
        element.clear()
        element.send_keys(val)

    def click_next_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.NEXT_BTN)
        element.click()

    def get_availability_zone_list(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.AVAILABILITY_ZONE)
        return element.text

    def select_zone(self, zone):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.ZONE_SELECT)
        select = Select(element)
        select.select_by_visible_text(zone)

    def click_vpc_radio_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.VPC_RADIO_BTN)
        element.click()

    def click_subnet_radio_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.SUBNET_RADIO_BTN)
        element.click()

    def click_security_grp_std_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.STD_RADIO_BTN)
        element.click()

    def click_security_grp_custom_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.CUSTOM_RADIO_BTN)
        element.click()

    def click_set_instance_option_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.SET_INSTANCE_OPTION_BTN)
        element.click()

    def click_slide_bar_3(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.SLIDE_BAR_CLICK_3)
        element.click()

    def type_host_name(self, host_name):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_NAME_INPUT)
        element.clear()
        element.send_keys(host_name)

    def type_host_desc(self, host_desc):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_DESC_INPUT)
        element.clear()
        element.send_keys(host_desc)

    def select_host_instance_type(self, instance_type):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_INSTANCE_TYPE_SELECT)
        select = Select(element)
        select.select_by_visible_text(instance_type)

    def type_host_mem_size(self, host_mem_size):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_MEM_SIZE_INPUT)
        element.clear()
        element.send_keys(host_mem_size)

    def click_create_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_CREATE_BTN)
        element.click()

    def get_host_status_text(self):
        xpath_loc = AmazonEc2Locators.Ec2Locators.STATUS_LABEL_PREFIX + "1" + AmazonEc2Locators.Ec2Locators.STATUS_LABEL_SUFFIX
        print xpath_loc
        by = (By.XPATH, xpath_loc)
        element = self.driver.find_element(*by)
        return element.text

    def get_host_status_element(self):
        xpath_loc = AmazonEc2Locators.Ec2Locators.STATUS_LABEL_PREFIX + "1" + AmazonEc2Locators.Ec2Locators.STATUS_LABEL_SUFFIX
        print xpath_loc
        by = (By.XPATH, xpath_loc)
        element = self.driver.find_element(*by)
        return element

    def check_creating_host(self, num_host):
        for x in range(1,num_host):
            xpath_loc = AmazonEc2Locators.Ec2Locators.CREATING_HOST_PREFIX + str(x) + AmazonEc2Locators.Ec2Locators.CREATING_HOST_SUFFIX
            print xpath_loc
            by = (By.XPATH, xpath_loc)
            element = self.driver.find_element(*by)
            cur_txt = element.text
            assert cur_txt, "CREATING"

    def wait_for_first_host_active(self, value):
        xpath_loc = AmazonEc2Locators.Ec2Locators.STATUS_LABEL_PREFIX + "1" + AmazonEc2Locators.Ec2Locators.STATUS_LABEL_SUFFIX
        print xpath_loc
        element = self.driver.find_element(xpath_loc)
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(element,value))

    # def wait_for_other_hosts_active(self, num_host, status):
    #     is_all_active = False
    #     sec = 0
    #     max_wait_time = 120
    #     while(is_all_active):
    #         for x in range(1,num_host):
    #             xpath_loc = AmazonEc2Locators.Ec2Locators.STATUS_LABEL_PREFIX + x + AmazonEc2Locators.Ec2Locators.STATUS_LABEL_SUFFIX
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
    #                 sec = sec + 1
    #
    #           if sec > max_wait_time:
    #              self.fail("time out")
    #              break


    def is_no_host_text_found(self):
        try:
            element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.NO_HOST_FOUND_TEXT)
            element.is_displayed()
            print "No Host Found"
            return True
        except Exception as e:
            print "No Host not Found"
            e.message
            return False

    def click_menu(self):
        status = self.get_host_status_element()
        hidden_menu = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.CLICK_MENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(status)
        actions.click(hidden_menu)
        actions.perform()

    def click_deactivate_link(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.DEACTIVATE_LINK)
        element.click()

    def click_delete_link(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.DELETE_LINK)
        element.click()

    def click_purge_link(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.PURGE_LINK)
        element.click()

    def click_delete_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.DELETE_BTN)
        element.click()

    def _host_delete(self):
        print "Inside _host_delete"
        host_status=  self.get_host_status_text()
        print host_status
        self.click_menu()
        time.sleep(2)
        if host_status == self.STATUS_ERROR:
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_ACTIVE:
            self.click_deactivate_link()
            time.sleep(2)
        elif host_status == self.STATUS_INACTIVE:
            self.click_delete_link()
            time.sleep(2)
        elif host_status == self.STATUS_REMOVED:
            self.click_purge_link()
            time.sleep(2)

        if host_status != self.STATUS_REMOVED:
            self.click_delete_btn()
            time.sleep(2)

    def host_delete(self):
        print "Inside host_delete"
        sec = 0
        while ((self.is_no_host_text_found()) or (sec < self.MAX_WAIT_TIME)):
            print "Calling _host_delete"
            self._host_delete()
            print "_host_delete complete"
            sec = sec + 1
            time.sleep(1)





