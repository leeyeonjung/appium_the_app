# Standard library
import logging
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

# Third-party libraries
import pytest_check as check

log = logging.getLogger()


def test_webview_demo_placeholder(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # 입력창 element 지정
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")

    # Assertion: placeholder 값이 "https://appiumpro.com"인지 확인
    check.equal(inputfield.text, "https://appiumpro.com")


def test_webview_context(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # Assertion: 현재 driver context가 "WEBVIEW_com.appiumpro.the_app"인지 확인
    check.equal(wd.current_context, "WEBVIEW_com.appiumpro.the_app")


def test_get_certified(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Get Certified 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[1]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'Appium Pro Training, Tutorials, and Certification'인지 확인
    check.equal(title, 'Appium Pro Training, Tutorials, and Certification')


def test_subscribe(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[2]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'Subscribe Now'인지 확인
    check.equal(title, 'Subscribe Now')


def test_latest(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Latest 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[3]/a').click()

    sleep(1.0)

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'Edition 124'인지 확인
    check.equal(title, 'Edition 124')


def test_all_editions(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # All Editions 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[4]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'All Editions'인지 확인
    check.equal(title, 'All Editions')


def test_sponsors(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Sponsors 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[5]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'Sponsors'인지 확인
    check.equal(title, 'Sponsors')


def test_contact(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Contact 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[6]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'Contact Us'인지 확인
    check.equal(title, 'Contact Us')


def test_about(wd):
    # Webview Demo 화면 진입
    wd.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 주소 입력
    inputfield = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 클릭
    go_button = wd.find_element(AppiumBy.ACCESSIBILITY_ID, "navigateBtn")
    go_button.click()

    # context를 webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 햄버거 바 클릭
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/a/img').click()

    # About 메뉴 선택
    wd.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[7]/a').click()

    # 타이틀 텍스트 가져오기
    title = wd.find_element(By.XPATH, '/html/body/div/div/div[3]/h1').text

    # Assertion: title이 'About'인지 확인
    check.equal(title, 'About')