from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import logging

log = logging.getLogger()

# Appium Server URL
appium_server_url = 'http://localhost:4723'

def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.appiumpro.the_app"
    options.app_activity = "com.appiumpro.the_app.MainActivity"
    options.auto_grant_permissions = True

    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(5)
    return driver

# element 선택 함수는 driver와 각 값을 인자로 받아서 사용
def xpath(driver, data):
    return driver.find_element(By.XPATH, data)

def xpaths(driver, data):
    return driver.find_elements(By.XPATH, data)

def id(driver, data):
    return driver.find_element(AppiumBy.ID, data)

def acc_id(driver, data):
    return driver.find_element(AppiumBy.ACCESSIBILITY_ID, data)