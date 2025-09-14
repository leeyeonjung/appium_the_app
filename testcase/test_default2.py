import pytest_check as check
import pytest
import logging
import configuration.webDriver as webDriver

log = logging.getLogger()

def test_setup2():
    result=webDriver.call()
    check.equal("appium.webdriver.webdriver.WebDriver" in str(result), True)