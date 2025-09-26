# Standard library
import logging

# Third-party libraries
import pytest_check as check

# Local modules
from tests.common_util import find_elements as element

log = logging.getLogger()

def test_context_webview(wd):

    #Photo Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    inputfield = element.acc_id(wd, "urlInput")

    inputfield.send_keys("https://appiumpro.com")

    go_button = element.acc_id(wd, "navigateBtn")

    go_button.click()

    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    check.equal(wd.current_context, "WEBVIEW_com.appiumpro.the_app")


def test_subscribe_01(wd):

    #Photo Demo 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    inputfield = element.acc_id(wd, "urlInput")

    inputfield.send_keys("https://appiumpro.com")

    go_button = element.acc_id(wd, "navigateBtn")

    go_button.click()

    log.info(wd.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.appiumpro.the_app']
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")
    log.info(wd.current_context)

    element.xpath(wd, '/html/body/div/div/div[2]/div/div/a/img').click()

    # sidebar = element.xpath(wd, '//*[@id="__next"]/div/div[2]/div') 
    # check.equal(sidebar.is_displayed(), True)



# # 햄버거 바 클릭하기
# def test_subscribe_01(wd):

#     # App Session 실행
#     wd = webdriver.create_driver() 

#     #Photo Demo 화면 진입
#     element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

#     inputfield = element.acc_id(wd, "urlInput")

#     inputfield.send_keys("https://appiumpro.com")

#     go_button = element.acc_id(wd, "navigateBtn")

#     go_button.click()

#     log.info(wd.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.appiumpro.the_app']
#     wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")
#     log.info(wd.current_context)

#     element.xpath(wd, '//*[@id="toggleMenu"]/img').click()

#     html = wd.page_source
#     log.info(html[:1000])  # 앞부분만 출력해서 확인

