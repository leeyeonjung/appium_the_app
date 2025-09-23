# 표준 라이브러리
import logging
import os
from io import BytesIO
from time import sleep
from pathlib import Path

# 외부 라이브러리
import pytest_check as check
from PIL import Image

# 내부 모듈
from tests.configuration import webDriver as webdriver
from tests.common_util import control_image as control_image

log = logging.getLogger()

BASE_DIR = Path(__file__).resolve().parent.parent  # tests/
IMAGE_DIR = BASE_DIR / "image"

def test_image_01():

    # App Session 실행
    wd = webdriver.create_driver() 

    #Photo Demo 화면 진입
    webdriver.xpath(wd,'(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]').click()
    sleep(0.5)

    expected = {
        str(IMAGE_DIR / "original_1.jpg"),
        str(IMAGE_DIR / "original_2.jpg"),
        str(IMAGE_DIR / "original_3.jpg"),
        str(IMAGE_DIR / "original_4.jpg"),
        str(IMAGE_DIR / "original_5.jpg"),
        str(IMAGE_DIR / "original_6.jpg"),
    }

    # ScrollView 안의 모든 ImageView 가져오기
    elements = webdriver.xpaths(wd, "//android.widget.ScrollView//android.widget.ImageView")
    log.info(elements)

    used_elements = set()
    found = set()

    for ref in expected:
        best_score = -1
        best_el = None

        for idx, el in enumerate(elements, start=1):
            if idx in used_elements:
                continue

            screenshot = control_image.open(BytesIO(el.screenshot_as_png)).convert("RGB")
            score = control_image.compare(screenshot, ref)

            # 매번 점수 로그 찍기
            log.info(f"[Compare] {ref} vs element {idx} → {score:.2f}")

            if score > best_score:
                best_score = score
                best_el = idx

        # 최종 매칭 결과
        if best_score >= 90:
            used_elements.add(best_el)
            found.add(ref)
            log.info(f"[PASS] {ref} matched with element {best_el} (score {best_score:.2f})")
        else:
            log.warning(f"[FAIL] {ref} best match was element {best_el} (score {best_score:.2f})")

    # 마지막에 전체 결과 확인
    log.info(f"Found: {found}")
    check.equal(found, expected, f"Not all images matched correctly. Found: {found}")

    # App Session 종료
    wd.quit()


def test_image_text_01():

    # App Session 실행
    wd = webdriver.create_driver() 

    #Photo Demo 화면 진입
    webdriver.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]').click()
    sleep(0.5)

    expected = {
        str(IMAGE_DIR / "original_1.jpg"),
        str(IMAGE_DIR / "original_2.jpg"),
        str(IMAGE_DIR / "original_3.jpg"),
        str(IMAGE_DIR / "original_4.jpg"),
        str(IMAGE_DIR / "original_5.jpg"),
        str(IMAGE_DIR / "original_6.jpg"),
    }

    # ScrollView 안의 모든 ImageView 가져오기
    elements = webdriver.xpaths(wd, "//android.widget.ScrollView//android.widget.ImageView")
    log.info(f"elements count = {len(elements)}")

    # Expected Text 
    expected_texts = {
        "original_1.jpg": "This is a picture of: 2 tanker ships with snowy mountains in the background",
        "original_2.jpg": "This is a picture of: Wispy clouds in a blue sky",
        "original_3.jpg": "This is a picture of: English bay with snowy mountains",
        "original_4.jpg": "This is a picture of: The Vancouver skyline at sunrise",
        "original_5.jpg": "This is a picture of: A long thin cloud below mountain level",
        "original_6.jpg": "This is a picture of: Imposing mountains and West Vancouver"
    }

    used_elements = set()

    for ref in expected:
        best_score = -1
        best_el = None

        # 🚩 매 루프마다 fresh elements 다시 가져오기
        elements = webdriver.xpaths(wd, "//android.widget.ScrollView//android.widget.ImageView")
        log.info(f"elements count = {len(elements)}")

        for idx, el in enumerate(elements, start=1):
            if idx in used_elements:
                continue

            screenshot = control_image.open(BytesIO(el.screenshot_as_png)).convert("RGB")
            score = control_image.compare(screenshot, ref)

            log.info(f"[Compare] {ref} vs element {idx} → {score:.2f}")

            if score > best_score:
                best_score = score
                best_el = idx

        if best_score >= 90:
            used_elements.add(best_el)
            log.info(f"[PASS] {ref} matched with element {best_el} (score {best_score:.2f})")

            # fresh elements 다시 조회 → stale 방지
            elements = webdriver.xpaths(wd, "//android.widget.ScrollView//android.widget.ImageView")
            target_el = elements[best_el - 1]
            target_el.click()
            log.info(f"Clicked element {best_el} for {ref}")

            # 결과 텍스트 확인
            result_text_element = webdriver.xpath(
                wd, '//android.widget.TextView[@resource-id="android:id/message"]'
            )
            result_text = result_text_element.text.strip()

            ref_filename = os.path.basename(ref)
            expected_text = expected_texts[ref_filename]

            check.equal(result_text, expected_text, f"[CHECK FAIL] {ref_filename}")
            log.info(f"[CHECK PASS] {ref_filename}: Got expected text '{result_text}'")

            # 🚩 OK 버튼 눌러서 다이얼로그 닫기
            ok_button = webdriver.xpath(wd, '//android.widget.Button[@resource-id="android:id/button1"]')
            ok_button.click()
            log.info("Dialog closed with OK button")
        else:
            log.warning(f"[FAIL] {ref} best match was element {best_el} (score {best_score:.2f})")

    # App Session 종료
    wd.quit()

# def test_image_01():
# def test_image_01():
# def test_image_01():