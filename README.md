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
| Device | **Android Emulator / Physical Device** |

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
│   │           └── ...
│
├── requirements.txt                             # 테스트 환경 의존성 정의 파일
│
├── Jenkinsfile                                  # Jenkins Pipeline Groovy 파일 (CI/CD 자동화 스크립트)
│
└── README.md                                    # 프로젝트 개요, 구조, 실행 방법 등 문서화 파일
```

---

## 🔍 Key Features

### 1️⃣ **Appium 자동화 테스트**
- Appium에서 공식 제공하는 *The App* 일부 기능을 테스트 대상으로 선정  
- 각 화면 진입 및 UI 요소 검증 자동화  

### 2️⃣ **Pytest 기반 모듈화 구조**
- `conftest.py`에서 **driver fixture**를 관리  
- 각 기능별 테스트는 독립 실행 가능 (e.g: `pytest /tests/testcase/test_2_login_screen.py::test_into_login_screen`)   

### 3️⃣ **HTML Report & Video Recording**
- 실행 시 자동으로 HTML 리포트 생성  
- 각 테스트 함수별 실행 과정을 녹화하여 디버깅에 활용 가능  
- 결과는 `tests/Result/` 하위 폴더에 자동 저장  
  - 📊 HTML Report → `test-reports/`
  - 🎥 Video Report → `video-reports/`

### 4️⃣ **CI 환경 (Jenkins + AWS + 로컬 테스트 실행)**
- AWS EC2 (Ubuntu)에 **Jenkins를 구축**하여 테스트를 원격으로 제어하도록 구성  
- Jenkins는 **명령 제어 역할**을 수행하며, 실제 테스트는 **Windows 로컬 PC**에서 실행  
- 로컬 PC에는 **Appium Server, Android Emulator, Pytest 환경**이 구동되어 있으며,  
  Jenkins에서 원격 명령으로 pytest를 실행하여 테스트를 수행  
- 테스트 결과(HTML Report 및 동영상)는 로컬 환경의 `tests/Result/test-reports` 폴더에 자동 생성  
- Jenkins 콘솔에서는 실행 로그를 통해 테스트 진행 상황을 실시간으로 확인 가능

---

## 🔐 Jenkins CI Server (on AWS)
| 항목 | 정보 |
|------|------|
| **Jenkins URL** | 🔗 [http://3.36.219.242:8080](http://3.36.219.242:8080) |
| **User ID** | `admin` |
| **Password** | `admin` |
| **Trigger** | GitHub Push 이벤트 기반 (테스트 전용 repo와 연동) |
| **Execution Flow** | Jenkins → Remote Windows (pytest 실행) → 로컬 환경에서 생성된 HTML Report 수집 → Jenkins에서 표시 |

📦 Jenkinsfile은 **트리거 역할을 하는 테스트 전용 저장소**에 위치하며,  
이 저장소의 Jenkinsfile과 현재 [`appium_the_app`](https://github.com/leeyeonjung/appium_the_app) 저장소에 포함된 Jenkinsfile은 **동일한 내용**으로 관리됩니다.  

---

## 🚀 How to Run

### ▶️ 로컬 실행
```bash
pip install -r /tests/requirements.txt
pytest
```

### ▶️ Docker 기반 Appium Server 실행 (Linux/Mac)
```bash
cd appium_server
docker compose up -d
```

### ▶️ Jenkins 원격 실행 (AWS EC2)
- AWS EC2에 구축된 Jenkins에서 **Windows 로컬 테스트 환경을 원격으로 제어**하여 테스트를 실행 
- 테스트 결과(HTML Report 및 동영상)는 실행환경의 `tests/Result/` 폴더에 저장된 html report 중 가장 최근 파일을 Jenkins 서버로 가지고와 결과를 확인할 수 있음
- Jenkins 콘솔 로그를 통해 테스트 진행 상황과 결과 요약을 실시간으로 확인 가능

---

## 📊 Test Results
| 항목 | 설명 |
|------|------|
| **HTML Report** | `tests/Result/test-reports/` 폴더 자동 생성 |
| **Video Report** | `tests/Result/video-reports/` 폴더 자동 생성 |
| **Sample Reports** | [📁 GitHub Result 폴더](https://github.com/leeyeonjung/appium_the_app/tree/main/tests/Result) |

---

## 💡 Future Improvement
- iOS 환경 자동화 (Appium + XCUITest)
- Allure Report 적용
- 테스트 케이스 Excel 연동 통한 테스트 결과 업데이트

---

## 👩‍💻 Author
**이연정 (YJ)**  
- QA Automation Engineer  
- 📧 Contact: asa48284828@gmail.com
