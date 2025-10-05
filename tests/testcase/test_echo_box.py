# Standard library
import logging
import time

# Third-party libraries
import pytest_check as check

# Local modules
from tests.common_util import find_elements as element

log = logging.getLogger()


def test_into_echo_box(wd):
    # Echo Box 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]').click()

    # Action_bar_root 아래 자식 TextView element 지정
    title = element.xpath(
        wd,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView'
    )
    
    # Assertion: Title text가 "Echo Screen"인지 확인
    check.equal(title.text, "Echo Screen")


def test_echo_box_placeholder(wd):
    # Echo Box 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]').click()

    # 입력창 element 지정
    inputfield = element.acc_id(wd, "messageInput")

    # Assertion: placeholder 값이 "Say something"인지 확인
    check.equal(inputfield.text, "Say something")


def test_inputfield_function_01(wd):
    # Echo Box 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]').click()

    # 입력할 텍스트 정의
    input_text = "Hello Test1"

    # 입력창 element 지정
    inputfield = element.acc_id(wd, "messageInput")

    # 입력창에 텍스트 입력
    inputfield.send_keys(input_text)

    # 저장 버튼 element 지정
    saveBtn = element.acc_id(wd, "messageSaveBtn")

    # 저장 버튼 클릭
    saveBtn.click()

    # 저장 처리 대기 (0.5초)
    time.sleep(0.5)
    
    # 저장된 메시지 element 지정
    result = element.xpath(wd, "//*[@resource-id='savedMessage']")

    # Assertion: 저장된 메시지가 입력 텍스트와 동일한지 확인
    check.equal(result.text, input_text)


def test_inputfield_function_02(wd):
    # Echo Box 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[1]').click()

    # 첫 번째 입력 텍스트 정의
    input_text1 = "Hello Test1"
    # 두 번째 입력 텍스트 정의
    input_text2 = "Hello Test2"

    # 첫 번째 텍스트 입력 및 저장
    inputfield = element.acc_id(wd, "messageInput")
    inputfield.send_keys(input_text1)
    saveBtn = element.acc_id(wd, "messageSaveBtn")
    saveBtn.click()

    # 저장 처리 대기 (0.5초)
    time.sleep(0.5)
    
    # 두 번째 텍스트 입력 및 저장
    inputfield = element.acc_id(wd, "messageInput")
    inputfield.send_keys(input_text2)
    saveBtn = element.acc_id(wd, "messageSaveBtn")
    saveBtn.click()

    # 저장된 메시지 element 지정
    result = element.xpath(wd, "//*[@resource-id='savedMessage']")

    # Assertion: 저장된 메시지가 두 번째 입력 텍스트와 동일한지 확인
    check.equal(result.text, input_text2)
