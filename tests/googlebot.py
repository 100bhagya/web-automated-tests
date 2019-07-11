import requests
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options, DesiredCapabilities


class testing_googlebot(cls):
    driver = webdriver.Remote
    url = ""
    @classmethod
    def setUpClass(cls):
        useragent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        options = Options()
        options.add_argument('user-agent= ' + useragent)
        cls.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        cls.switch_url = {
            "live" : "www",
            "stage" : "stage",
            "dev" : "dev"
        }
        cls.api = cls.switch.get(sys.argv[1])

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_home_page(self):
        url = "https://" + self.api + ".dailyobjects.com/"
        self.driver.get(url)
        self.assertIn('header-row', self.driver.page_source)
        self.assertIn('do-logo', self.driver.page_source)
        self.assertIn('Hot Selling', self.driver.page_source)

    def test_product_page(self):
        url = "https://" + self.api + ".dailyobjects.com/dailyobjects-teal-blue-glass-case-cover-for-iphone-x"
        self.driver.get(url)
        self.assertIn('ngx-json-ld', self.driver.page_source)

    def test_listing_page(self):
        url = "https://" + self.api + ".dailyobjects.com/designer-cases/apple/iphone-x/glass"
        self.driver.get(url)
        response = requests.get(url)
        if response.ok:
            print(response.status_code)
        else:
            print('Bad Response')


if __name__ == "__main__":
    url = sys.argv[1]
    unittest.main(argv=[url])
