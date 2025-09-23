# appium_the_app

## Appium Server 실행
1. Docker 설치
2. Appium_Server의 Dockerfile build
  - docker build -t my-appium:3.0.2 .
3. Appium_Server의 docker-compose.yml 파일로 docker container 실행 (localhost:4723으로 port 지정 되어 있음)
  - docker-compose up -d


## Version Information
- Python **3.13.7**
- Appium **3.0.2**


## Requirements
의존성 패키지는 requirements.txt를 참고하세요.
아래 명령어로 설치할 수 있습니다
- pip install -r requirements.txt


## Running Tests
- 이 프로젝트는 pytest 기반의 테스트를 사용합니다.
가장 상위 경로의 run_tests.py 스크립트를 실행하면 전체 테스트가 실행되며,
결과는 tests 하위에 📊test-reports📊 폴더에 HTML 리포트(report_YYYY-MM-DD_HH-MM-SS.html) 로 자동 생성됩니다.
(폴더가 없다면 자동 생성 됩니다.)
- 전체 테스트 케이스 실행 명령어
  - python run_tests.py
- 특정 파일만 실행
  - python run_tests.py {특정 파일 경로}
  - e.g) python run_tests.py testcase/test_login.py
- 특정 파일의 특정 함수만 실행
  - python run_tests.py {특정 파일 경로}::{특정 함수}
  - e.g) python run_tests.py testcase/test_login.py::test_setup
