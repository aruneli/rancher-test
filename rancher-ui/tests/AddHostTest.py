__author__ = 'aruneli'

import unittest
from selenium import webdriver
from pages import WelcomePage
from pages import InfraPage
from pages import AmazonEc2AddHost
import time

class AddHostTest(unittest.TestCase):

    def setUp(self):
        base_url = "http://54.68.100.87:8080"
        welcome_url = "/static/apps/welcome"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        print self.driver
        self.driver.get(base_url + welcome_url)
        time.sleep(2)

    def test_add_host(self):
        self.welcome_page = WelcomePage.WelcomePage(self.driver)
        assert self.welcome_page.is_title_matches(), "Rancher"
        self.welcome_page.click_infra_tab()
        time.sleep(2)
        self.infra_page = InfraPage.InfraPage(self.driver)
        self.infra_page.click_add_host()
        time.sleep(2)
        cur_text = self.infra_page.get_add_host_hdr()
        assert cur_text, "Add Host"
        self.infra_page.click_ec2_img()
        time.sleep(6)
        self.aec2_add_host = AmazonEc2AddHost.AmazonEc2AddHost(self.driver)
        self.aec2_add_host.type_access_key("AKIAI54MYS73NAP2ABHA")
        self.aec2_add_host.type_secret_key("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")
        self.aec2_add_host.click_next_btn()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()