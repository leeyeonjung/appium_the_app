import os
import sys
import base64
import pytest
import logging
from datetime import datetime
from pathlib import Path
from pytest_html import extras
from appium import webdriver
from appium.options.android import UiAutomator2Options

log = logging.getLogger(__name__)

# ==============================
# 📂 전역 프로젝트 루트 (tests 하위)
# ==============================
BASE_DIR = Path(__file__).resolve().parents[0]

# ==============================
# 📱 멀티 디바이스 설정
# ==============================
devices = [
    pytest.param(
        {"udid": "emulator-5554", "systemPort": 8200, "server_url": "http://127.0.0.1:4723"},
        id="emulator-5554"
    ),
    pytest.param(
        {"udid": "R3CX306FV2J", "systemPort": 8201, "server_url": "http://127.0.0.1:4725"},
        id="R3CX306FV2J"
    ),
]

# ==============================
# 📱 Appium Driver fixture
# ==============================
@pytest.fixture(params=devices)
def wd(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = request.param["udid"]
    options.system_port = request.param["systemPort"]
    options.app_package = "com.appiumpro.the_app"
    options.app_activity = "com.appiumpro.the_app.MainActivity"
    options.auto_grant_permissions = True
    options.no_reset = False

    driver = webdriver.Remote(request.param["server_url"], options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

# ==============================
# 🎥 Test Video Recording Fixture
# ==============================
@pytest.fixture(autouse=True)
def record_video(request, wd):
    # 테스트 스크립트 파일명
    file_name = Path(request.node.fspath).stem

    # 기기 식별자
    device_id = wd.capabilities.get("udid") or wd.capabilities.get("deviceUDID") or "unknown_device"

    # === Result/🎥video-reports🎥/{device_id}/{테스트 파일명}/ ===
    save_dir = BASE_DIR / "Result" / "🎥video-reports🎥" / device_id / file_name
    os.makedirs(save_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = request.node.originalname or request.node.name
    safe_name = "".join(c for c in test_name if c.isalnum() or c in ("_", "-"))

    save_path = save_dir / f"{safe_name}_{timestamp}.mp4"

    wd.start_recording_screen()
    yield
    video_raw = wd.stop_recording_screen()

    with open(save_path, "wb") as f:
        f.write(base64.b64decode(video_raw))

    log.info(f"[VIDEO] {device_id} → {safe_name} 실행 동영상 저장 완료 → {save_path}")

    # pytest-html report에 동영상 링크 추가
    rel_path = os.path.relpath(save_path, BASE_DIR)
    if hasattr(request.node, "extra"):
        request.node.extra.append(extras.url(rel_path, name=f"📹 {device_id} 동영상"))
    else:
        request.node.extra = [extras.url(rel_path, name=f"📹 {device_id} 동영상")]


# ==============================
# 📌 pytest 실행 시 항상 HTML Report 자동 생성
# ==============================
def pytest_configure(config):
    # CLI에서 --html 옵션 안 준 경우 자동으로 생성
    if not getattr(config.option, "htmlpath", None):
        report_dir = BASE_DIR / "Result" / "📊test-reports📊"
        report_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = report_dir / f"report_{timestamp}.html"

        # 옵션 주입
        config.option.htmlpath = str(report_path)
        config.option.self_contained_html = True