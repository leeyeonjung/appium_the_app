# Standard library
import logging

# Third-party libraries
import pytest_check as check

# Local modules
from tests.common_util import find_elements as element

log = logging.getLogger()


def test_setup(wd):
    # Assertion: 실행 session 안에 "appium.webdriver.webdriver.WebDriver" 존재
    check.equal("appium.webdriver.webdriver.WebDriver" in str(wd), True)


def test_homescreen_01(wd):
    # 첫 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]//android.widget.TextView[@resource-id="listItemTitle"]'

    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)

    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Echo Box"
    check.equal(elements[0].text, "Echo Box")
    # Assertion: Description이 "Write something and save to local memory"
    check.equal(elements[1].text, "Write something and save to local memory")


def test_homescreen_02(wd):
    # 두 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]//android.widget.TextView[@resource-id="listItemTitle"]'

    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)

    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Login Screen"
    check.equal(elements[0].text, "Login Screen")
    # Assertion: Description이 "A fake login screen for testing"
    check.equal(elements[1].text, "A fake login screen for testing")


def test_homescreen_03(wd):
    # 세 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[3]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Clipboard Demo"
    check.equal(elements[0].text, "Clipboard Demo")
    # Assertion: Description이 "Mess around with the clipboard"
    check.equal(elements[1].text, "Mess around with the clipboard")


def test_homescreen_04(wd):
    # 네 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Webview Demo"
    check.equal(elements[0].text, "Webview Demo")
    # Assertion: Description이 "Explore the possibilities of hybrid apps"
    check.equal(elements[1].text, "Explore the possibilities of hybrid apps")


def test_homescreen_05(wd):
    # 다섯 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[5]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Dual Webview Demo"
    check.equal(elements[0].text, "Dual Webview Demo")
    # Assertion: Description이 "Automate apps with multiple webviews"
    check.equal(elements[1].text, "Automate apps with multiple webviews")


def test_homescreen_06(wd):
    # 여섯 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[6]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "List Demo"
    check.equal(elements[0].text, "List Demo")
    # Assertion: Description이 "Scroll through a list of stuff"
    check.equal(elements[1].text, "Scroll through a list of stuff")


def test_homescreen_07(wd):
    # 일곱 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Photo Demo"
    check.equal(elements[0].text, "Photo Demo")
    # Assertion: Description이 "Some photos with no distinguishing IDs"
    check.equal(elements[1].text, "Some photos with no distinguishing IDs")


def test_homescreen_08(wd):
    # 여덟 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[8]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Geolocation Demo"
    check.equal(elements[0].text, "Geolocation Demo")
    # Assertion: Description이 "See your current location"
    check.equal(elements[1].text, "See your current location")


def test_homescreen_09(wd):
    # 아홉 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[9]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Picker Demo"
    check.equal(elements[0].text, "Picker Demo")
    # Assertion: Description이 "Use some picker wheels for fun and profit"
    check.equal(elements[1].text, "Use some picker wheels for fun and profit")


def test_homescreen_10(wd):
    # 열 번째 ViewGroup 안의 TextView 찾기
    value = '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[10]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가져오기
    elements = element.xpaths(wd, value)
    
    # elements의 각 내용을 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Assertion: Title이 "Verify Phone Number"
    check.equal(elements[0].text, "Verify Phone Number")
    # Assertion: Description이 "A fake SMS auto-verification screen"
    check.equal(elements[1].text, "A fake SMS auto-verification screen")