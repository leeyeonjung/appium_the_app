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
    
    # Assertion : Title text가 "Login"임
    check.equal(title.text, "Login")


def test_login_screen_placeholder(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # id 입력란 element 조회
    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    # password 입력란 element 조회
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")

    # Assertion : id 입력란의 placeholder가 Username임
    check.equal(idfield.text, "Username")
    # Assertion : password 입력란의 placeholder가 Password임
    check.equal(pwfield.text, "Password")


def test_login_success(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # id 입력 필드 element를 조회하여 idfield 변수에 할당
    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    # id 입력란에 유효한 id (alice) 입력
    idfield.send_keys("alice")
    sleep(1.0)

    # 비밀번호 입력 필드 element를 조회하여 pwfield 변수에 할당
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    # pw 입력란에 유효한 pw (mypassword) 입력    
    pwfield.send_keys("mypassword")
    sleep(1.0)

    # login 버튼 element를 조회하여 loginbtn 변수에 할당
    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    # loginbtn 클릭
    loginbtn.click()
    sleep(1.0)

    # 화면의 FrameLayout 찾기
    container = wd.find_element(
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout'
    )

    # 내부 TextView 텍스트들 수집
    texts = [el.text for el in container.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")]
    log.info(texts)

    # Assertion : 로그인 성공하여 조회된 화면에 "Secret Area" 와 "You are logged in as alice" text가 조회됨
    check.equal("Secret Area" in texts, True)
    check.equal("You are logged in as alice" in texts, True)


def test_logout_success(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # id 입력 필드 element를 조회하여 idfield 변수에 할당
    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    # id 입력란에 유효한 id (alice) 입력
    idfield.send_keys("alice")
    sleep(1.0)

    # 비밀번호 입력 필드 element를 조회하여 pwfield 변수에 할당
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    # pw 입력란에 유효한 pw (mypassword) 입력    
    pwfield.send_keys("mypassword")
    sleep(1.0)

    # login 버튼 element를 조회하여 loginbtn 변수에 할당
    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    # loginbtn 클릭
    loginbtn.click()
    sleep(1.0)

    # logout 버튼 element를 조회하여 logoutbtn 변수에 할당
    logoutbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "Logout")
    # logoutbtn 클릭
    logoutbtn.click()
    sleep(1.0)

    # Action_bar_root 아래 자식 TextView의 locator path를 title로 지정
    title = wd.find_element(By.XPATH,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView')
    
    # Assertion : 로그아웃되어 다시 로그인 화면으로 진입 후, Title text가 "Login"임
    check.equal(title.text, "Login")


def test_login_fail(wd):

    # Login Screen 화면 진입
    wd.find_element(By.XPATH,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # id 입력 필드 element를 조회하여 idfield 변수에 할당
    idfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
    # id 입력란에 유효한 id (alice) 입력
    idfield.send_keys("alice")
    sleep(1.0)

    # 비밀번호 입력 필드 element를 조회하여 pwfield 변수에 할당
    pwfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
    # pw 입력란에 비유효한 pw (test) 입력    
    pwfield.send_keys("test")
    sleep(1.0)

    # login 버튼 element를 조회하여 loginbtn 변수에 할당
    loginbtn = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    # loginbtn 클릭
    loginbtn.click()
    sleep(1.0)

    # alert 메시지 조회하여 alertmsg 변수에 할당
    alertmsg = wd.find_element(AppiumBy.ID, "android:id/message")

    # Assertion : alertmsg가 "Invalid login credentials, please try again" 임
    check.equal(alertmsg.text, "Invalid login credentials, please try again")