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


@test(groups=["DigitalOcean"])
class DigitalTestHostAddDelete (object):

    @test
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.digital_handle = DigitalOceanPage.DigitalOcean(self.driver)
        self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
        self.infra_page = InfraPage.InfraPage(self.driver)
        self.welcome_page = WelcomePage.WelcomePage(self.driver)

    @test
    def test_add_digital_host(self):
        try:
            print "Inside test_add_digital_ocean"
            self.driver.get(constants.host_add_DigitalOcean_url)
            self.digital_handle.select_quantity()
            self.digital_handle.click_slide_bar()
            self.digital_handle.input_host_name("DHost01")
            self.digital_handle.input_host_desc("DigitalOcean Hosts")
            self.digital_handle.input_access_token("a1a7c625c612c3d9a07300f1396fff2ff129342c63d4516b3101fdb61b1f2a48")
            self.digital_handle.select_image("ubuntu-14-04-x64")
            self.digital_handle.select_host_mem_size("16gb")
            self.digital_handle.select_region("San Francisco 1")
            self.digital_handle.click_create_btn()
            time.sleep(10)
            print "DigitalOcean Hosts add complete"
        except Exception as ex:
            traceback.print_exc()

    @test(depends_on=[test_add_digital_host])
    def test_del_host(self):
        self.driver.get(constants.RancherServerBaseURL + constants.welcome_url)
        self.driver.get(constants.inventory_url)
        time.sleep(2)
        print "Going to delete hosts"
        self.infra_hosts_handle.host_delete()
        print "Hosts delete complete"

    @test(depends_on=[test_del_host], always_run=True)
    def shutdown(self):
        print "Inside tearDown"
        self.driver.close()


def test_host_add_delete():
    from proboscis import TestProgram

    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == '__main__':
    test_host_add_delete()
