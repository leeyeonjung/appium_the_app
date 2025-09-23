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


def test_homescreen_01():

    # App Session 실행
    wd = webdriver.create_driver()

    # 첫번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]//android.widget.TextView[@resource-id="listItemTitle"]'

    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)

    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Echo Box"
    check.equal(elements[0].text, "Echo Box")
    # Result : element의 description이 "Write something and save to local memory"
    check.equal(elements[1].text, "Write something and save to local memory")

    # App Session 종료
    wd.quit()


def test_homescreen_02():

    # App Session 실행
    wd = webdriver.create_driver()

    # 두번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]//android.widget.TextView[@resource-id="listItemTitle"]'

    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)

    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Login Screen"
    check.equal(elements[0].text, "Login Screen")
    # Result : element의 description이 "A fake login screen for testing"
    check.equal(elements[1].text, "A fake login screen for testing")

    
    # App Session 종료
    wd.quit()


def test_homescreen_03():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[3]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Clipboard Demo"
    check.equal(elements[0].text, "Clipboard Demo")
    # Result : element의 description이 "Mess around with the clipboard"
    check.equal(elements[1].text, "Mess around with the clipboard")
    
    # App Session 종료
    wd.quit()


def test_homescreen_04():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Webview Demo"
    check.equal(elements[0].text, "Webview Demo")
    # Result : element의 description이 "Explore the possibilities of hybrid apps"
    check.equal(elements[1].text, "Explore the possibilities of hybrid apps")
    
    # App Session 종료
    wd.quit()


def test_homescreen_05():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[5]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Dual Webview Demo"
    check.equal(elements[0].text, "Dual Webview Demo")
    # Result : element의 description이 "Automate apps with multiple webviews"
    check.equal(elements[1].text, "Automate apps with multiple webviews")
    
    # App Session 종료
    wd.quit()


def test_homescreen_06():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[6]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "List Demo"
    check.equal(elements[0].text, "List Demo")
    # Result : element의 description이 "Scroll through a list of stuff"
    check.equal(elements[1].text, "Scroll through a list of stuff")
    
    # App Session 종료
    wd.quit()


def test_homescreen_07():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Photo Demo"
    check.equal(elements[0].text, "Photo Demo")
    # Result : element의 description이 "Some photos with no distinguishing IDs"
    check.equal(elements[1].text, "Some photos with no distinguishing IDs")
    
    # App Session 종료
    wd.quit()


def test_homescreen_08():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[8]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Geolocation Demo"
    check.equal(elements[0].text, "Geolocation Demo")
    # Result : element의 description이 "See your current location"
    check.equal(elements[1].text, "See your current location")
    
    # App Session 종료
    wd.quit()


def test_homescreen_09():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[9]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Picker Demo"
    check.equal(elements[0].text, "Picker Demo")
    # Result : element의 description이 "Use some picker wheels for fun and profit"
    check.equal(elements[1].text, "Use some picker wheels for fun and profit")
    
    # App Session 종료
    wd.quit()


def test_homescreen_10():
    
    # App Session 실행
    wd = webdriver.create_driver()

    # 첫 번째 ViewGroup 안의 TextView 찾기
    value='(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[10]//android.widget.TextView[@resource-id="listItemTitle"]'
    
    # xpath로 elements 요소 가지고 오기
    elements = webdriver.xpaths(wd, value)
    
    # elements의 각 내용 log로 출력
    for idx, el in enumerate(elements, start=1):
        log.debug(f"Element {idx}: text={el.text}, resource-id={el.get_attribute('resource-id')}")

    # Result : Title이 "Verify Phone Number"
    check.equal(elements[0].text, "Verify Phone Number")
    # Result : element의 description이 "A fake SMS auto-verification screen"
    check.equal(elements[1].text, "A fake SMS auto-verification screen")
    wd.quit()