from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import argparse
import time

API_KEY = ''

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--install', type=bool, default=False, help='Automatically download, install and configure the appropriate browser drivers')

args = parser.parse_args()

if args.install:
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    browser = webdriver.Firefox()

url = 'http://localhost/reCaptcha-demo/index.php'

browser.get(url)

dataSiteKey = browser.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')

"""
solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(API_KEY)
solver.set_website_url(url)
solver.set_website_key(dataSiteKey)

response = solver.solve_and_return_solution()

if response != 0:
    browser.execute_script(f"document.getElementById('g-recaptcha-response').innetHTML ='{response}'")
else:
    print(solver.err_string)
"""

if API_KEY == '':
    gRecaptchaResponse = ''

    while gRecaptchaResponse == '':
        gRecaptchaResponse = browser.execute_script("var elem = document.getElementById('g-recaptcha-response'); return elem ? elem.value : false;")
        time.sleep(1)

    if(not gRecaptchaResponse):
        print("Element 'g-recaptcha-response' not found!")
        browser.quit()
        exit()

    browser.execute_script(f"alert('{gRecaptchaResponse}')")

    time.sleep(20)
    browser.quit()