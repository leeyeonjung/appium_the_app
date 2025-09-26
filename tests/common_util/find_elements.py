from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import logging

log = logging.getLogger()

# element 선택 함수는 driver와 각 값을 인자로 받아서 사용
def xpath(driver, data):
    return driver.find_element(By.XPATH, data)

def xpaths(driver, data):
    return driver.find_elements(By.XPATH, data)

def id(driver, data):
    return driver.find_element(AppiumBy.ID, data)

def acc_id(driver, data):
    return driver.find_element(AppiumBy.ACCESSIBILITY_ID, data)