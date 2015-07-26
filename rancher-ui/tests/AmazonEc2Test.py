__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

import unittest
from selenium import webdriver
from pages import WelcomePage
from pages import InfraPage
from pages import AmazonEc2 as EC2
import time

class AmazonEc2Host(unittest.TestCase):

    base_url = "http://54.68.100.87:8080"
    welcome_url = "/static/apps/welcome"
    inventory_url = base_url + "/static/infra/hosts"


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        print self.driver
        time.sleep(2)

    # def test_add_host(self):
    #     self.driver.get(self.base_url + self.welcome_url)
    #     self.welcome_page = WelcomePage.WelcomePage(self.driver)
    #     assert self.welcome_page.is_title_matches(), "Rancher"
    #     self.welcome_page.click_infra_tab()
    #     time.sleep(2)
    #     self.infra_page = InfraPage.InfraPage(self.driver)
    #     self.infra_page.click_add_host()
    #     time.sleep(2)
    #     cur_text = self.infra_page.get_add_host_hdr()
    #     assert cur_text, "Add Host"
    #     self.infra_page.click_ec2_img()
    #     time.sleep(2)
    #     self.aec2_add_host = EC2.AmazonEc2(self.driver)
    #     self.aec2_add_host.type_access_key("AKIAI54MYS73NAP2ABHA")
    #     self.aec2_add_host.type_secret_key("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")
    #     self.aec2_add_host.click_next_btn()
    #     time.sleep(2)
    #     cur_text = self.aec2_add_host.get_availability_zone_list()
    #     print cur_text
    #     assert cur_text, "Availability zone & vpc".capitalize()
    #     self.aec2_add_host.select_zone("us-west-2a")
    #     self.aec2_add_host.click_vpc_radio_btn()
    #     self.aec2_add_host.click_set_instance_option_btn()
    #     self.aec2_add_host.click_next_btn()
    #     time.sleep(5)
    #     self.aec2_add_host.click_slide_bar_3()
    #     self.aec2_add_host.type_host_name("host01")
    #     self.aec2_add_host.type_host_desc("Test Hosts")
    #     self.aec2_add_host.type_host_mem_size("16")
    #     self.aec2_add_host.select_host_instance_type("t2.small")
    #     self.aec2_add_host.click_create_btn()
    #     time.sleep(10)
    #     self.aec2_add_host.check_creating_host(3)
    #     time.sleep(2)
    #     self.aec2_add_host.wait_for_first_host_active("ACTIVE")
    #     time.sleep(60)
    #     self.aec2_add_host.host_delete()

    def test_del_host(self):
        self.driver.get(self.base_url + self.welcome_url)
        self.driver.get(self.inventory_url)
        time.sleep(2)
        self.aec2_add_host = EC2.AmazonEc2(self.driver)
        print "Going to delete hosts"
        self.aec2_add_host.host_delete()
        print "Hosts delete complete"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()