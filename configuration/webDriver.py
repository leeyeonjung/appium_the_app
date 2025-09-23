from appium import webdriver
from selenium.webdriver.common.by import By
import pytest
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

# 헬퍼 함수들은 driver를 인자로 받도록 바꾸기
def xpath(driver, data):
    return driver.find_element(By.XPATH, data)

def xpaths(driver, data):
    return driver.find_elements(By.XPATH, data)

def id(driver, data):
    return driver.find_elements(By.ID, data)
    
#webDriver.wd.close_app() / 앱 종료
#webDriver.wd.launch_app() / 앱 백그라운드에서 재시작
#webDriver.wd.reset() 
# ['NATIVE_APP', 'WEBVIEW_kr.co.nicevan.bujaapp']