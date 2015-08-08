__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from proboscis import test
from selenium import webdriver
from pages import InfraHostsPage
from pages import WelcomePage
from pages import InfraPage
from pages import AmazonEc2Page
from pages import DigitalOceanPage
from pages import HostRegistrationPage
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
import constants


# @test(groups=["DigitalOcean"])
# class DigitalTestHostAddDelete (object):
#
#     @test
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(10)
#         self.digital_handle = DigitalOceanPage.DigitalOcean(self.driver)
#         self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
#         self.infra_page = InfraPage.InfraPage(self.driver)
#         self.welcome_page = WelcomePage.WelcomePage(self.driver)
#
#     @test
#     def test_add_digital_host(self):
#         try:
#             print "Inside test_add_digital_ocean"
#             self.driver.get(constants.host_add_DigitalOcean_url)
#             self.digital_handle.select_quantity()
#             self.digital_handle.click_slide_bar()
#             self.digital_handle.input_host_name("DHost01")
#             self.digital_handle.input_host_desc("DigitalOcean Hosts")
#             self.digital_handle.input_access_token("a1a7c625c612c3d9a07300f1396fff2ff129342c63d4516b3101fdb61b1f2a48")
#             self.digital_handle.select_image("ubuntu-14-04-x64")
#             self.digital_handle.select_host_mem_size("16gb")
#             self.digital_handle.select_region("San Francisco 1")
#             self.digital_handle.click_create_btn()
#             time.sleep(10)
#             print "DigitalOcean Hosts add complete"
#         except Exception as ex:
#             traceback.print_exc()
#
#     @test(depends_on=[test_add_digital_host])
#     def test_del_host(self):
#         self.driver.get(constants.RancherServerBaseURL + constants.welcome_url)
#         self.driver.get(constants.inventory_url)
#         time.sleep(2)
#         print "Going to delete hosts"
#         self.infra_hosts_handle.host_delete()
#         print "Hosts delete complete"
#
#     @test(depends_on=[test_del_host], always_run=True)
#     def shutdown(self):
#         print "Inside tearDown"
#         self.driver.close()


@test(groups=["EC2"])
class EC2TestHostAddDelete (object):

    @test
    def init(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(constants.welcome_url)
        self.welcome_page = WelcomePage.WelcomePage(self.driver)

    @test(groups=["EC2"], depends_on=[init])
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
        self.ec2_handle.input_access_key("AKIAI54MYS73NAP2ABHA")
        self.ec2_handle.input_secret_key("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")
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
        self.infra_hosts_handle.wait_for_first_host_active("ACTIVE")
        print "EC2 Hosts add complete"
        self.driver.close()

    def shutdown(self):
        print "Inside tearDown"
        self.driver.close()

    def test_del_host(self):
        self.driver.get(constants.RancherServerBaseURL + constants.welcome_url)
        self.driver.get(constants.inventory_url)
        time.sleep(2)
        print "Going to delete hosts"
        self.infra_hosts_handle.host_delete()
        print "Hosts delete complete"

# @test(groups=["Packet"])
# class PacketTestHostAddDelete (object):
#
#     @test
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(10)
#         self.digital_handle = DigitalOceanPage.DigitalOcean(self.driver)
#         self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
#         self.infra_page = InfraPage.InfraPage(self.driver)
#         self.welcome_page = WelcomePage.WelcomePage(self.driver)
#
#     @test
#     def test_add_digital_host(self):
#         try:
#             print "Inside test_add_digital_ocean"
#             self.driver.get(constants.host_add_Packet_url)
#             self.digital_handle.select_quantity()
#             self.digital_handle.click_slide_bar()
#             self.digital_handle.input_host_name("DHost01")
#             self.digital_handle.input_host_desc("DigitalOcean Hosts")
#             self.digital_handle.input_access_token("a1a7c625c612c3d9a07300f1396fff2ff129342c63d4516b3101fdb61b1f2a48")
#             self.digital_handle.select_image("ubuntu-14-04-x64")
#             self.digital_handle.select_host_mem_size("16gb")
#             self.digital_handle.select_region("San Francisco 1")
#             self.digital_handle.click_create_btn()
#             time.sleep(10)
#             print "DigitalOcean Hosts add complete"
#         except Exception as ex:
#             traceback.print_exc()
#
#     @test(depends_on=[test_add_digital_host])
#     def test_del_host(self):
#         self.driver.get(constants.RancherServerBaseURL + constants.welcome_url)
#         self.driver.get(constants.inventory_url)
#         time.sleep(2)
#         print "Going to delete hosts"
#         self.infra_hosts_handle.host_delete()
#         print "Hosts delete complete"
#
#     @test(depends_on=[test_del_host], always_run=True)
#     def shutdown(self):
#         print "Inside tearDown"
#         self.driver.close()
#
# @test(groups=["Rackspace"])
# class RackspaceTestHostAddDelete (object):
#
#     @test
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(10)
#         self.digital_handle = DigitalOceanPage.DigitalOcean(self.driver)
#         self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
#         self.infra_page = InfraPage.InfraPage(self.driver)
#         self.welcome_page = WelcomePage.WelcomePage(self.driver)
#
#     @test
#     def test_add_digital_host(self):
#         try:
#             print "Inside test_add_digital_ocean"
#             self.driver.get(constants.host_add_Rackspace_url)
#             self.digital_handle.select_quantity()
#             self.digital_handle.click_slide_bar()
#             self.digital_handle.input_host_name("DHost01")
#             self.digital_handle.input_host_desc("DigitalOcean Hosts")
#             self.digital_handle.input_access_token("a1a7c625c612c3d9a07300f1396fff2ff129342c63d4516b3101fdb61b1f2a48")
#             self.digital_handle.select_image("ubuntu-14-04-x64")
#             self.digital_handle.select_host_mem_size("16gb")
#             self.digital_handle.select_region("San Francisco 1")
#             self.digital_handle.click_create_btn()
#             time.sleep(10)
#             print "DigitalOcean Hosts add complete"
#         except Exception as ex:
#             traceback.print_exc()
#
#     @test(depends_on=[test_add_digital_host])
#     def test_del_host(self):
#         self.driver.get(constants.RancherServerBaseURL + constants.welcome_url)
#         self.driver.get(constants.inventory_url)
#         time.sleep(2)
#         print "Going to delete hosts"
#         self.infra_hosts_handle.host_delete()
#         print "Hosts delete complete"
#
#     @test(depends_on=[test_del_host], always_run=True)
#     def shutdown(self):
#         print "Inside tearDown"
#         self.driver.close()


def test_host_add_delete():
    from proboscis import TestProgram

    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == '__main__':
    test_host_add_delete()
