import time
import constants
import unittest
from selenium import webdriver
from pages import InfraHostsPage

class test(unittest.TestCase):

    def test_del_host(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(constants.inventory_url)
        time.sleep(2)
        print "Going to delete hosts"
        self.infra_hosts_handle = InfraHostsPage.InfraHostsPage(self.driver)
        time.sleep(2)
        self.infra_hosts_handle.host_delete()
        print "Hosts delete complete"
        self.driver.close()

if __name__ == "__main__":
    unittest.main()




