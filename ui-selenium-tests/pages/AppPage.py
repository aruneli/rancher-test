__author__ = 'Arunkumar Eli'
__email__ = "elrarun@gmail.com"

from pages import BasePage


class AppPage(BasePage):

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
