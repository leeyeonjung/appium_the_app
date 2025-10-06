# Standard library
import logging
import os
from io import BytesIO
from time import sleep
from pathlib import Path

# Third-party libraries
import pytest_check as check

# Local modules
from tests.common_util import find_elements as element
from tests.common_util import control_image as control_image

log = logging.getLogger()


BASE_DIR = Path(__file__).resolve().parents[1]  # BASE_DIR : tests/ 하위 경로
IMAGE_DIR = BASE_DIR / "image"  # IMAGE_DIR : 비교할 original image 경로


def test_into_photo_demo(wd):
    # Photo Demo 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]').click()

    # Action_bar_root 아래 자식 TextView element 지정
    title = element.xpath(
        wd,
        '//android.widget.LinearLayout[@resource-id="com.appiumpro.the_app:id/action_bar_root"]//android.widget.TextView'
    )

    # Assertion: Title text가 "Photo Library. Tap a photo!"인지 확인
    check.equal(title.text, "Photo Library. Tap a photo!")


def test_photo(wd):

    # 폴더 구분을 위한 기기 udid 저장
    raw_device_id = wd.capabilities.get("udid") or wd.capabilities.get("deviceUDID") or "unknown_device"
    device_id = str(raw_device_id).replace(":", "_").replace("/", "_").replace("\\", "_")

    # 캡쳐 이미지 저장 경로 정의
    save_dir = BASE_DIR / "Result" / "📸image📸" / device_id / "test_photo"
    save_dir.mkdir(parents=True, exist_ok=True)

    # Photo Demo 화면 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]').click()
    sleep(1)

    # 비교할 원본 이미지 경로
    expected = {
        str(IMAGE_DIR / "original_1.png"),
        str(IMAGE_DIR / "original_2.png"),
        str(IMAGE_DIR / "original_3.png"),
        str(IMAGE_DIR / "original_4.png"),
        str(IMAGE_DIR / "original_5.png"),
        str(IMAGE_DIR / "original_6.png"),
    }

    # swipe를 위한 기기 해상도 조회
    win = wd.get_window_rect()
    win_w, win_h = win["width"], win["height"]
    log.info(f"📱 Window size: {win_w}x{win_h}")

    captured, seen_rects, verified_images = set(), set(), set()

    # 정사각형으로 노출된 이미지는 저장 (기존에 저장 된 이미지는 저장하지 않도록 중복 방지 처리)
    def capture_visible_images():
        elements = element.xpaths(wd, "//android.widget.ScrollView//android.widget.ImageView")
        log.info(f"[SCAN] Found {len(elements)} ImageViews")

        for el in elements:
            rect = el.rect
            x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]
            bottom, right = y + h, x + w

            fully_visible = (x >= -10 and y >= 0 and right <= win_w + 10 and bottom <= win_h + 30)
            square_like = abs(w - h) < 20
            if not (fully_visible and square_like):
                continue

            # 중복 판별 강화 (좌표 오차 허용)
            duplicate_found = False
            for (sx, sy, sw, sh) in seen_rects:
                # 좌표 오차 ±25px, 크기 오차 ±10px 이내면 동일 이미지로 간주하여 저장 하지 않음
                if abs(sx - x) < 25 and abs(sy - y) < 25 and abs(sw - w) < 10 and abs(sh - h) < 10:
                    duplicate_found = True
                    break
            if duplicate_found:
                log.info(f"[SKIP] Duplicate image detected at (x={x}, y={y})")
                continue

            # 중복 아닌 경우에는 이미지 저장
            path = save_dir / f"captured_{len(captured)+1}.png"
            with open(path, "wb") as f:
                f.write(el.screenshot_as_png)
            seen_rects.add((x, y, w, h))
            captured.add(str(path))
            log.info(f"[SAVE] {path.name} ({w}x{h}) at (x={x}, y={y})")

    # 스와이프 동작 (Appium 3.x 버전 해당)
    def swipe(step=0.45):
        start_x = win_w // 2
        start_y = int(win_h * 0.75)
        end_y = int(win_h * (0.75 - step))
        log.info(f"[SWIPE] ({start_x},{start_y}) → ({start_x},{end_y})")
        wd.swipe(start_x, start_y, start_x, end_y, 900)
        sleep(1.2)

    # 스크롤하며 이미지 수집
    for _ in range(6):
        before = len(captured)
        capture_visible_images()
        if len(captured) >= 6:
            log.info("All 6 images captured.")
            break
        swipe(step=0.45)
        after = len(captured)
        if after == before:
            log.info("No new images detected after swipe.")
            break

    log.info(f"Captured {len(captured)} images in total.")

    # control_image.py 이용한 이미지 비교 (SSIM)
    for ref in expected:
        best_score, best_path = -1, None
        for path in captured:
            screenshot = control_image.open(path).convert("RGB")
            score = control_image.compare(screenshot, ref)
            if score > best_score:
                best_score, best_path = score, path

    # 이미지 비교 score가 90 이상인 경우 verified_images에 추가
        if best_score >= 90:
            verified_images.add(ref)
            log.info(f"[PASS] {ref} matched {best_path} ({best_score:.2f})")
        else:
            log.warning(f"[FAIL] {ref} best {best_path} ({best_score:.2f})")

    expected_count = len(expected)
    log.info(f"📊 Verified {len(verified_images)} / {expected_count} images.")

    # Assertion: 실제 확인 된 image가 6개 인지 확인
    check.equal(verified_images, expected, f"[VERIFY FAIL] Some images not matched. Found: {verified_images}")


def test_image_text(wd):

    # 폴더 구분을 위한 기기 udid 저장
    raw_device_id = wd.capabilities.get("udid") or wd.capabilities.get("deviceUDID") or "unknown_device"
    device_id = str(raw_device_id).replace(":", "_").replace("/", "_").replace("\\", "_")

    # 캡쳐 이미지 저장 경로 정의
    save_dir = BASE_DIR / "Result" / "📸image📸" / device_id / "test_image_text"
    save_dir.mkdir(parents=True, exist_ok=True)

    # Photo Demo 진입
    element.xpath(wd, '(//android.view.ViewGroup[@resource-id="RNE__LISTITEM__padView"])[7]').click()
    sleep(1)

    expected_texts = {
        "original_1.png": "This is a picture of: 2 tanker ships with snowy mountains in the background",
        "original_2.png": "This is a picture of: Wispy clouds in a blue sky",
        "original_3.png": "This is a picture of: English bay with snowy mountains",
        "original_4.png": "This is a picture of: The Vancouver skyline at sunrise",
        "original_5.png": "This is a picture of: A long thin cloud below mountain level",
        "original_6.png": "This is a picture of: Imposing mountains and West Vancouver"
    }

    # IMAGE_DIR + expected_texts의 key 값으로 원본이미지 확인
    expected_images = [str(IMAGE_DIR / name) for name in expected_texts.keys()]

    # swipe를 위한 기기 해상도 조회
    win = wd.get_window_rect()
    win_w, win_h = win["width"], win["height"]

    captured, seen_rects = set(), set()
    matched_count = 0

    # 스와이프 동작 (Appium 3.x 버전 해당)
    def swipe(step=0.45):
        start_x = win_w // 2
        start_y = int(win_h * 0.75)
        end_y = int(win_h * (0.75 - step))
        log.info(f"[SWIPE short] ({start_x},{start_y}) → ({start_x},{end_y})")
        wd.swipe(start_x, start_y, start_x, end_y, 800)
        sleep(1.2)

    # 이미지 비교와 text 검증 (기존에 저장 된 이미지는 확인하지 않도록 중복 방지 처리)
    def capture_and_check():
        nonlocal matched_count
        elements = element.xpaths(wd, "//android.widget.ImageView")
        log.info(f"[SCAN] Found {len(elements)} ImageViews")

        for el in elements:
            rect = el.rect
            x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]
            bottom, right = y + h, x + w

            fully_visible = (x >= -10 and y >= 0 and right <= win_w + 10 and bottom <= win_h + 30)
            square_like = abs(w - h) < 20
            if not (fully_visible and square_like):
                continue

            # 중복 판별 강화 (좌표 오차 허용)
            duplicate_found = False
            for (sx, sy, sw, sh) in seen_rects:
                # 좌표 오차 ±25px, 크기 오차 ±10px 이내면 동일 이미지로 간주
                if abs(sx - x) < 25 and abs(sy - y) < 25 and abs(sw - w) < 10 and abs(sh - h) < 10:
                    duplicate_found = True
                    break
            if duplicate_found:
                continue

            # 중복 아닌 경우 이미지 저장
            path = save_dir / f"captured_{len(captured)+1}.png"
            with open(path, "wb") as f:
                f.write(el.screenshot_as_png)
            seen_rects.add((x, y, w, h))
            captured.add(str(path))
            log.info(f"[SAVE] {path.name} ({w}x{h}) at (x={x}, y={y})")

            # 원본 이미지와 비교하여 클릭 후, text 비교
            screenshot = control_image.open(path).convert("RGB")
            best_score, matched_ref = -1, None
            for ref in expected_images:
                ref_name = os.path.basename(ref)
                if ref_name in verified_texts:
                    continue
                score = control_image.compare(screenshot, ref)
                if score > best_score:
                    best_score, matched_ref = score, ref
            if best_score < 85 or matched_ref is None:
                log.warning(f"[SKIP] {path.name} similarity too low ({best_score:.2f})")
                continue

            matched_name = os.path.basename(matched_ref)
            expected_text = expected_texts[matched_name]
            log.info(f"[MATCH] {path.name} ↔ {matched_name} ({best_score:.2f})")

            el.click()
            sleep(0.5)
            dialog = element.xpath(wd, '//android.widget.TextView[@resource-id="android:id/message"]')
            actual = dialog.text.strip()
            check.equal(actual, expected_text, f"[TEXT FAIL] {matched_name}")
            log.info(f"[TEXT PASS] {matched_name}: '{actual}'")

            ok = element.xpath(wd, '//android.widget.Button[@resource-id="android:id/button1"]')
            ok.click()
            sleep(0.8)

            verified_texts.add(matched_name)
            matched_count += 1

    # 스크롤 반복 — 새 이미지 없으면 중단
    verified_texts = set()

    for _ in range(6):
        before = len(verified_texts)
        capture_and_check()

        # 모든 expected text가 통과되면 중단
        if len(verified_texts) >= len(expected_texts):
            log.info("✅ All expected images verified. Stopping scroll.")
            break

        swipe(step=0.45)
        after = len(verified_texts)
        if after == before:
            log.info("🔚 No new verifications after swipe. Stopping.")
            break

    expected_count = len(expected_texts)
    log.info(f"📸 Captured {len(captured)} images, verified {matched_count}")
    # Assertion: 실제 확인 된 image가 6개 인지 확인
    check.equal(len(verified_texts), expected_count,
                f"[VERIFY FAIL] Only {len(verified_texts)}/{expected_count} verified")
    log.info("All expected images successfully captured and verified.")
