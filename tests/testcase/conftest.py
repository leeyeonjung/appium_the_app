# conftest.py
import pytest
import os
import base64
from datetime import datetime
from pathlib import Path
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options

log = logging.getLogger()


appium_server_url = "http://127.0.0.1:4723"

# === Appium Driver fixture ===
@pytest.fixture
def wd():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.appiumpro.the_app"
    options.app_activity = "com.appiumpro.the_app.MainActivity"
    options.auto_grant_permissions = True

    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def record_video(request, wd):
    # === 프로젝트 루트 기준 (tests 와 같은 depth) ===
    BASE_DIR = Path(__file__).resolve().parents[2]

    # === Result/🎥video-reports🎥 폴더 보장 ===
    save_dir = BASE_DIR / "Result" / "🎥video-reports🎥"
    os.makedirs(save_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = request.node.name
    save_path = save_dir / f"{test_name}_{timestamp}.mp4"

    wd.start_recording_screen()
    yield
    video_raw = wd.stop_recording_screen()
    with open(save_path, "wb") as f:
        f.write(base64.b64decode(video_raw))

    log.info(f"[VIDEO] {test_name} 실행 동영상 저장 완료 → {save_path}")