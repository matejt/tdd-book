from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

binary = r'C:\Users\dhdyk0\AppData\Local\Mozilla Firefox\firefox.exe'
options = Options()
options.binary = binary

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True

browser = webdriver.Firefox(capabilities=cap, options=options)
browser.get('http://localhost:8000')
assert 'Django' in browser.title
