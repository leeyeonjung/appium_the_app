# Standard library
import logging
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

# Third-party libraries
import pytest_check as check

log = logging.getLogger()


def test_into_login_screen(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # Action_bar_root 아래 자식 TextView의 locator path를 title로 지정
    title = wd.find_element(By.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView')
    
    # Assertion : Title text가 "Login"인지 확인
    check.equal(title.text, "Login")


def test_login_screen_placeholder(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")

    check.equal(idfield.text, "Username")
    check.equal(pwfield.text, "Password")


def test_login_success(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    idfield.send_keys("alice")
    sleep(1.0)
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    pwfield.send_keys("mypassword")
    sleep(1.0)

    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    loginbtn.click()
    sleep(1.0)

    # 1️⃣ 대상 FrameLayout 찾기
    container = wd.find_element(
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout'
    )

    # 2️⃣ 내부 TextView 텍스트들 수집
    texts = [el.text for el in container.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")]
    log.info(texts)

    # Assertion : 
    check.equal("Secret Area" in texts, True)
    check.equal("You are logged in as alice" in texts, True)


def test_logout_success(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    idfield.send_keys("alice")
    sleep(1.0)
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    pwfield.send_keys("mypassword")
    sleep(1.0)

    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    loginbtn.click()
    sleep(1.0)

    logoutbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "Logout")
    logoutbtn.click()
    sleep(1.0)

    # Action_bar_root 아래 자식 TextView의 locator path를 title로 지정
    title = wd.find_element(By.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView')
    
    # Assertion : Title text가 "Login"인지 확인
    check.equal(title.text, "Login")


def test_login_fail(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    idfield.send_keys("alice")
    sleep(1.0)
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    pwfield.send_keys("test")
    sleep(1.0)

    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    loginbtn.click()
    sleep(1.0)

    alertmsg = wd.find_element(AppiumBy.ID, "android:id/message")
    check.equal(alertmsg.text, "Invalid login credentials, please try again")