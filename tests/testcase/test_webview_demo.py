import pytest_check as check
import logging
from tests.configuration import webDriver as webdriver

log = logging.getLogger()

def test_webview_01():

    # App Session 실행
    wd = webdriver.create_driver() 

    #Photo Demo 화면 진입
    webdriver.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[4]').click()

    element = webdriver.acc_id(wd, "urlInput")

    element.send_keys("https://appiumpro.com")

    go_button = webdriver.acc_id(wd, "navigateBtn")

    go_button.click()

    log.info(wd.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.appiumpro.the_app']
    wd.switch_to.context("WEBVIEW_com.appiumpro.the_app")

    html = wd.page_source
    log.info(html[:1000])  # 앞부분만 출력해서 확인
