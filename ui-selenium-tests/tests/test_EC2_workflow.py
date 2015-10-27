__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from selenium import webdriver
from pages import InfraHostsPage
from pages import WelcomePage
from pages import InfraPage
from pages import AmazonEc2Page
from pages import AppPage
from pages import AddServicePage
from pages import HostRegistrationPage
import time
import constants
import logging
from proboscis import test
from selenium import webdriver
from pages import InfraHostsPage
from pages import WelcomePage
from pages import InfraPage
from pages import AmazonEc2Page
from pages import DigitalOceanPage
import time
import traceback
from datetime import datetime
import random
import types
import unittest
from proboscis.asserts import assert_equal
from proboscis.asserts import assert_false
from proboscis.asserts import assert_raises
from proboscis.asserts import assert_true
from proboscis import after_class
from proboscis import before_class
from proboscis import SkipTest
from proboscis import test


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

@test(groups=["EC2"])
class TestEC2 (object):

    @test
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(constants.welcome_url)
        self.welcome_page = WelcomePage.WelcomePage(self.driver)

    @test
    def test_add_ec2_host(self):
        assert self.welcome_page.is_title_matches(), "Rancher"
        self.welcome_page.click_infra_tab()
        time.sleep(1)
        self.infra_handle = InfraPage.InfraPage(self.driver)
        self.infra_handle.click_add_host()

        try:
            self.host_registration_handle = HostRegistrationPage.HostRegistration(self.driver)
            access_control_txt = self.host_registration_handle.get_access_control_txt()
            host_reg_txt = self.host_registration_handle.get_host_registration_txt()

            if "Access Control" in access_control_txt and "Host Registration" in host_reg_txt:
                self.host_registration_handle.click_save_btn()
                time.sleep(1)
        except Exception as ex:
            print "Host Registration page not found"

        self.infra_handle = InfraPage.InfraPage(self.driver)
        cur_text = self.infra_handle.get_add_host_hdr()
        assert cur_text, "Add Host"
        self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
        try:
            self.infra_hosts_handle.click_ec2_img()
            time.sleep(2)
        except Exception as ex:
            print "Not clicked"

        self.ec2_handle = AmazonEc2Page.AmazonEc2(self.driver)
        self.ec2_handle.input_access_key(constants.AWSAccessKeyId)
        self.ec2_handle.input_secret_key(constants.AWSSecretKey)
        self.ec2_handle.click_next_btn()
        time.sleep(2)
        cur_text = self.ec2_handle.get_availability_zone_list()
        print cur_text
        assert cur_text, "Availability zone & vpc".capitalize()
        self.ec2_handle.select_zone("us-west-2a")
        self.ec2_handle.click_vpc_radio_btn()
        self.ec2_handle.click_set_instance_option_btn()
        self.ec2_handle.click_next_btn()
        time.sleep(5)
        self.ec2_handle.click_slide_bar_3()
        self.ec2_handle.input_host_name("EHost01")
        self.ec2_handle.input_host_desc("Test Hosts")
        self.ec2_handle.input_host_mem_size("16")
        self.ec2_handle.select_host_instance_type("t2.small")
        self.ec2_handle.click_create_btn()
        time.sleep(10)
        self.infra_hosts_handle.check_creating_host(1)
        time.sleep(2)
        #self.infra_hosts_handle.wait_for_first_host_active("BOOTSTRAPPING")
        #self.infra_hosts_handle.wait_for_first_host_active("ACTIVE")
        print "EC2 Hosts add complete"

    @test(depends_on=[test_add_ec2_host])
    def test_virtual_host_routing_lb(self):
        self.service_handle = AddServicePage.AddService(self.driver)
        self.service_handle.input_service_name("mongo")
        self.service_handle.input_service_description("mongo db")
        self.service_handle.click_slide_bar_3()
        self.service_handle.input_image_name("mongo:latest")
        self.service_handle.click_create_btn()
        time.sleep(5)
        assert_equal(_is_service_created(), True)


    def _is_service_created(self):

    def teardown(self):
        print "Inside tearDown"
        self.driver.close()


def run_tests():
    from proboscis import TestProgram

    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == '__main__':
    run_tests()
