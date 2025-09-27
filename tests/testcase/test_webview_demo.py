# Standard library
import logging

# Third-party libraries
import pytest_check as check
import time

# Local modules
from tests.common_util import find_elements as element

log = logging.getLogger()

def test_webview_context(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # Assertion : 현재 driver의 "WEBVIEW_com.appiumpro.the_app"로 전환되어 웹뷰 정상적으로 노출 됨
    check.equal(wd.current_context, "WEBVIEW_com.appiumpro.the_app")


def test_get_certified(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Get Certified! 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[1]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'Appium Pro Training, Tutorials, and Certification'
    check.equal(title, 'Appium Pro Training, Tutorials, and Certification')


def test_subscribe(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[2]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'Subscribe Now'
    check.equal(title, 'Subscribe Now')


def test_latest(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[3]/a').click()

    time.sleep(1.0)

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'Edition 124'
    check.equal(title, 'Edition 124')


def test_all_editions(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[4]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'All Editions'
    check.equal(title, 'All Editions')


def test_sponsors(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[5]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'Sponsors'
    check.equal(title, 'Sponsors')


def test_contact(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[6]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'Contact Us'
    check.equal(title, 'Contact Us')


def test_about(wd):

    #Webview Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    # url 입력 필드에 "https://appiumpro.com" 입력
    inputfield = element.acc_id(wd, "urlInput")
    inputfield.send_keys("https://appiumpro.com")

    # Go 버튼 선택
    go_button = element.acc_id(wd, "navigateBtn")
    go_button.click()

    # context webview로 전환
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    # 우측 햄버거 바 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # Subscribe 선택
    element.xpath(wd, '/html/body/div/div/div[2]/div/ul/li[7]/a').click()

    # title 확인
    title = (element.xpath(wd, '/html/body/div/div/div[3]/h1')).text

    # Assertion : title이 'About'
    check.equal(title, 'About')