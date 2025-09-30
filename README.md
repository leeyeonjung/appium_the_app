# Appium The App Test Project

## Overview
이 프로젝트는 **Appium, Python, Pytest**를 이용하여 Appium에서 공식적으로 배포하는 샘플 앱 **The App**의 일부 기능을 자동화 테스트한 것입니다.  

테스트 결과는 **HTML Report**로 생성되며, 각 테스트 함수 실행 과정은 **동영상으로 기록**되어 디버깅 및 결과 검증에 활용할 수 있습니다.

---

## Version Information
- Python **3.13.7**  
- Appium **3.0.2**

---

## Clone Repository
```bash
git clone https://github.com/leeyeonjung/appium_the_app.git
cd appium_the_app
```

---

## Requirements
의존성 패키지는 `requirements.txt`를 참고하세요.  
아래 명령어로 설치할 수 있습니다:  
```bash
pip install -r requirements.txt
```

---

## APK
- `apk/` 디렉토리에는 **Appium에서 공식 제공하는 The App을 빌드한 APK 파일**이 포함되어 있습니다.  
- 원본 소스코드와 빌드 방법은 Appium 공식 저장소에서 확인할 수 있습니다:  
  👉 [Appium Sample Apps (The App)](https://github.com/appium/appium/tree/master/packages/appium/sample-code/apps)

---

## Test Code
- `tests/testcase/` 디렉토리에는 **대분류 메뉴별 테스트 코드**가 파일로 구분되어 있습니다. 
  (예: test_app_start.py, test_photo_demo.py test_webview_demo.py)

- 주요 테스트 파일 설명:
  - **test_app_start.py**  
    앱 실행 및 각 대분류 화면의 메뉴명과 설명을 검증하는 테스트 코드
  - **test_photo_demo.py**  
    `tests/image` 폴더에 원본 이미지를 두고, 해당 화면 진입 시 이미지가 정상적으로 표시되는지 확인하며,  
    각 이미지를 선택했을 때의 설명이 기대 결과와 일치하는지 검증하는 테스트 코드
  - **test_webview_demo.py**  
    webview_demo 화면 진입 후 URL 입력 시 기대한 웹페이지로 전환되는지 확인하고,  
    해당 웹페이지의 각 화면이 기대 결과와 일치하는지 검증하는 테스트 코드

---

## How To Run
`tests/run_tests.py` 스크립트를 실행하면 테스트가 동작합니다.  

- 전체 테스트 실행  
  ```bash
  python run_tests.py
  ```

- 특정 파일만 실행  
  ```bash
  python run_tests.py {특정 파일 경로}
  # 예시
  python run_tests.py testcase/test_login.py
  ```

- 특정 파일 내 특정 함수만 실행  
  ```bash
  python run_tests.py {특정 파일 경로}::{특정 함수}
  # 예시
  python run_tests.py testcase/test_login.py::test_setup
  ```

---

## Test Result
- `tests/Result/` 폴더는 존재하지 않을 경우 자동으로 생성됩니다.  

- **HTML Report**  
  - `tests/Result/📊test-reports📊/` 폴더에 저장  
  - 파일명은 실행 시간 기준: `report_YYYY-MM-DD_HH-MM-SS.html`  

- **Videos**  
  - `tests/Result/🎥video-reports🎥/` 폴더에 저장  
  - 파일명에는 실행 시간과 테스트 함수명이 포함되어 각 실행 과정을 동영상으로 확인할 수 있습니다.
