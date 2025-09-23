# conftest.py
import pytest
from tests.configuration import webDriver as webdriver

@pytest.fixture
def wd():
    driver = webdriver.create_driver()
    yield driver     # ← test 함수에서 wd 사용
    driver.quit()    # ← test 끝난 뒤 항상 세션 종료