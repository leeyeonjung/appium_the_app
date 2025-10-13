# 📱 Appium Automated Test Project – *The App*

## 🧩 Overview
이 프로젝트는 **Appium, Python, Pytest**를 이용하여  
Appium에서 공식 배포하는 샘플 앱 **“The App”** 의 주요 기능을 자동화 테스트한 개인 프로젝트입니다.

- 테스트 결과는 **HTML Report**로 시각화됩니다.  
- 각 테스트 함수 실행 과정은 **동영상으로 기록되어 디버깅 및 검증에 활용**할 수 있습니다.  
- AWS EC2 환경에 **Jenkins CI 서버를 직접 구축**하여,  
  **로컬(Windows) 테스트 환경을 원격으로 제어 및 실행**할 수 있도록 구성했습니다.  
  (Appium Server, Emulator, Pytest 환경은 Windows PC에 구동되어 있으며, Jenkins는 원격 실행을 담당)

---

## ⚙️ Tech Stack
| 구분 | 사용 기술 |
|------|------------|
| Test Framework | **Pytest**, **Appium 3.0.2**, **uiautomator2** |
| Language | **Python 3.13.7** |
| CI/CD | **Jenkins (on AWS EC2, Ubuntu)** |
| Report | **pytest-html**, 동영상 녹화 |
| Device | Android Emulator / Physical Device |

---

## 🏗️ Project Structure
```
appium_the_app/
├── app/                                         
│   └── app-release.apk                          # 실제 테스트용 Appium 공식 샘플 APK 파일
│
├── appium_server/                               # Appium 서버 환경 구성 폴더
│   ├── docker-compose.yml                       # Appium Server Docker 환경 정의 파일
│   └── entrypoint.sh                            # Appium Server 컨테이너 초기화 스크립트
│
├── testcase_excel/                              
│   └── (Testcase)The_App.xlsm                   # 테스트 시나리오에 대한 테스트 케이스 문서
│
├── tests/                                       # 테스트 코드 및 결과 관리 폴더
│   ├── conftest.py                              # pytest 전역 설정 및 Appium driver fixture 정의
│   │
│   ├── common_util/                             # 공통 유틸리티 모듈
│   │   ├── control_image.py                     # 이미지 비교 (SSIM 기반 이미지 유사도 검증)
│   │
│   ├── image/                                   # baseline 이미지 저장 폴더 (비교 기준)
│   │   ├── original_1.png ~ original_6.png      # 테스트 비교용 기준 이미지 파일들
│   │
│   ├── testcase/                                # 기능별 테스트 모듈
│   │   ├── test_0_app_start.py                  # 앱 실행 및 초기 화면 테스트
│   │   ├── test_1_echo_box.py                   # Echo Box 기능 검증
│   │   ├── test_2_login_screen.py               # 로그인 화면 검증
│   │   ├── test_4_webview_demo.py               # WebView 기능 검증
│   │   └── test_7_photo_demo.py                 # Photo Demo 기능 검증
│   │
│   ├── Results/                                 # 실제 테스트 결과 저장 폴더 (HTML Report, 영상, 캡처 포함)
│   │   ├── image/                               # 테스트 실행 중 캡처 이미지 저장
│   │   │   ├── [device-1]/                      # 예: emulator-5554, localhost-5555 등 기기별 폴더
│   │   │   │   ├── [test_module]/               # 예: test_photo, test_image_text 등 테스트 모듈별 폴더
│   │   │   │   │   ├── captured_1.png           # 테스트 실행 중 캡처된 이미지
│   │   │   │   │   ├── captured_2.png
│   │   │   │   │   └── ...
│   │   │   │   └── [다른 테스트 모듈]/          # 다른 테스트 모듈의 캡처 이미지 폴더
│   │   │   │       └── ...
│   │   │   └── [device-2]/                      # 두 번째 테스트 기기 폴더
│   │   │       └── ...
│   │   │
│   │   ├── test-reports/                        # pytest HTML Report 저장 폴더
│   │   │   └── report_YYYY-MM-DD_HH-MM-SS.html  # 실행 시각 기준 자동 생성된 리포트 파일
│   │   │
│   │   └── video-reports/                       # 테스트 실행 중 녹화 영상 저장 폴더
│   │       ├── [device-1]/                      # 예: emulator-5554
│   │       │   ├── [test_case_name]/            # 예: test_0_app_start, test_login 등 케이스별 폴더
│   │       │   │   ├── test_[scene]_01_YYYY-MM-DD_HH-MM-SS.mp4  # 단계별 녹화 파일
│   │       │   │   ├── test_[scene]_02_YYYY-MM-DD_HH-MM-SS.mp4
│   │       │   │   └── ...
│   │       │   └── [다른 테스트 케이스]/        # 다른 테스트 케이스의 영상 폴더
│   │       │       └── ...
│   │       └── [device-2]/                      # 두 번째 테스트 기기 폴더
입력

---

## 👩‍💻 Author
**이연정 (YJ)**  
- QA Automation Engineer  
- 📧 Contact: asa48284828@gmail.com
