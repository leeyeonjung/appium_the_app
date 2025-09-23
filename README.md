# appium_the_app

## Version Information
- Python **3.13.7**
- Appium **3.0.2**


## Requirements
의존성 패키지는 [requirements.txt](./requirements.txt)를 참고하세요.
아래 명령어로 설치할 수 있습니다
pip install -r requirements.txt


## Running Tests
- 이 프로젝트는 pytest 기반의 테스트를 사용합니다.
가장 상위 경로의 run_tests.py 스크립트를 실행하면 전체 테스트가 실행되며,
결과는 동일 경로에 HTML 리포트(report_YYYY-MM-DD_HH-MM-SS.html) 로 자동 생성됩니다.
- 전체 실행
python run_tests.py
- 특정 파일만 실행
python run_tests.py {특정 파일 경로}
python run_tests.py testcase/test_login.py
- 특정 파일의 특정 함수만 실행
python run_tests.py {특정 파일 경로}::{특정 함수}
python run_tests.py testcase/test_login.py::test_setup