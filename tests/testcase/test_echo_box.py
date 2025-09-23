import pytest_check as check
import logging
from tests.configuration import webDriver as webdriver

log = logging.getLogger()

def test_setup():

    # App Session 실행
    wd = webdriver.create_driver()

    # Result : 실행 session 안에 "appium.webdriver.webdriver.WebDriver" 존재
    check.equal("appium.webdriver.webdriver.WebDriver" in str(wd), True)

    # App Session 종료
    wd.quit()
