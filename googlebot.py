from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
options.add_argument('user-agent= Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
driver = webdriver.Chrome(options=options)
driver.get("https://www.dailyobjects.com/")
html_source = driver.page_source
print (html_source)

if ('header-row' in html_source):
    print('Header row is present')
if ('do-logo' in html_source):
    print('DailyObjects logo is present')
if ('smartphone page' in html_source):
    print('Smartphone navigation item is present')
if ('Bags And Sleeves Page' in html_source):
    print('Bags and sleeves nav item is present')
if ('https://ik.imagekit.io/dailyobjects/Offers/22-06-19/extra-10-off-desktop.jpg?tr=bg-FFFFFF,pr-true,q-100' in html_source):
    print('Offer banner is present')
if ('bannerImage' in html_source):
    print('Carousel banner is present')