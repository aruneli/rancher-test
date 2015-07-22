__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from locators import AmazonEc2Locators
from selenium.webdriver.support.ui import Select


class AmazonEc2(object):

    def __init__(self, driver):
        self.driver = driver

    def input_access_key(self, val):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.ACCESS_KEY_INPUT)
        element.clear()
        element.send_keys(val)

    def input_secret_key(self,val):
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

    def input_host_name(self, host_name):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_NAME_INPUT)
        element.clear()
        element.send_keys(host_name)

    def input_host_desc(self, host_desc):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_DESC_INPUT)
        element.clear()
        element.send_keys(host_desc)

    def select_host_instance_type(self, instance_type):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_INSTANCE_TYPE_SELECT)
        select = Select(element)
        select.select_by_visible_text(instance_type)

    def input_host_mem_size(self, host_mem_size):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_MEM_SIZE_INPUT)
        element.clear()
        element.send_keys(host_mem_size)

    def click_create_btn(self):
        element = self.driver.find_element(*AmazonEc2Locators.Ec2Locators.HOST_CREATE_BTN)
        element.click()





