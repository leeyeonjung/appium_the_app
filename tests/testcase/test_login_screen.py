# Standard library
import logging

# Third-party libraries
import pytest_check as check
import time

# Local modules
from tests.common_util import find_elements as element

log = logging.getLogger()


def test_into_login_screen(wd):

    # Echo Box 화면 진입
    element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

    # Action_bar_root 아래 자식 TextView의 locator path를 title로 지정
    title = element.xpath(wd,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView')
    
    # Assertion : Title text가 "Login"인지 확인
    check.equal(title.text, "Login")


# def test_login_success(wd):

#     # Login Screen 화면 진입
#     element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

#     input_text = "Hello Test1"
#     inputfield = element.acc_id(wd, "messageInput")
#     inputfield.send_keys(input_text)

#     saveBtn = element.acc_id(wd, "messageSaveBtn")
#     saveBtn.click()

#     time.sleep(0.5)
    
#     result = element.xpath(wd, "//*[@resource-id='savedMessage']")
#     check.equal(result.text, input_text)


# def test_login_fail(wd):

#     # Login Screen 화면 진입
#     element.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[2]').click()

#     input_text = "Hello Test1"
#     inputfield = element.acc_id(wd, "messageInput")
#     inputfield.send_keys(input_text)

#     saveBtn = element.acc_id(wd, "messageSaveBtn")
#     saveBtn.click()

#     time.sleep(0.5)
    
#     result = element.xpath(wd, "//*[@resource-id='savedMessage']")
#     check.equal(result.text, input_text)

#     # 아이디 O / 비밀번호 O
    # alice / mypassword
    # 아이디 O / 비밀번호 X
    # 아이디 X / 비밀번호 O
    # 아이디 X / 비밀번호 X
    