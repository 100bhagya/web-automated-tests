import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options, DesiredCapabilities

switch = {
    "live" : "www",
    "stage" : "stage",
    "dev" : "dev"
}

api = switch.get(sys.argv[1])

url = "https://" + api + ".dailyobjects.com/"

options = Options()
options.add_argument(
    'user-agent= Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')

driver = webdriver.Remote(
    command_executor='http://0.0.0.0:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get(url)
html_source = driver.page_source

if 'header-row' in html_source:
    print('Header row is present')
if 'do-logo' in html_source:
    print('DailyObjects logo is present')
if 'smartphone page' in html_source:
    print('Smartphone navigation item is present')
if 'Bags And Sleeves Page' in html_source:
    print('Bags and sleeves nav item is present')
if 'bannerImage' in html_source:
    print('Carousel banner is present')
