# 📱 Appium Automated Test Project – *The App*

## 🧩 Overview
이 프로젝트는 **Appium, Python, Pytest**를 이용하여  
Appium에서 공식 배포하는 샘플 앱 **“The App”** 의 주요 기능을 자동화 테스트한 개인 프로젝트입니다.

- 테스트 결과는 **HTML Report** 형태로 시각화됩니다.  
- 각 테스트 함수의 실행 과정은 **동영상으로 기록되어 디버깅 및 검증에 활용**할 수 있습니다.  
- AWS EC2 환경에 **Jenkins CI 서버를 직접 구축**하여  
  **로컬(Windows) 테스트 환경을 원격으로 제어 및 실행**할 수 있도록 구성했습니다.  
  (Appium Server, Emulator, Pytest 환경은 Windows PC에서 구동되며, Jenkins는 원격 실행을 담당)

---

## 🔍 Key Features

### 1️⃣ **Appium 자동화 테스트**
- Appium에서 공식 제공하는 *The App* 일부 기능을 테스트 케이스로 구성했습니다.  
- 각 테스트 함수의 테스트 케이스는 `testcase_excel` 디렉터리 내 **xlsm 파일**에 정의되어 있습니다.  
- 화면 전환 및 UI 요소 검증을 자동화 코드로 구현했습니다.

### 2️⃣ **Pytest 기반 모듈화 구조**
- `conftest.py` 파일에서 **Appium 드라이버 관련 fixture를 정의 및 관리**합니다.

### 3️⃣ **HTML Report & Video Recording**
- 결과는 `tests/Result/` 하위 폴더에 생성됩니다.  
  - 📊 **HTML Report** → `tests/Result/test-reports/`  
    - 전체 테스트 결과가 **시각화된 HTML 형태로 저장**됩니다.  
  - 🎥 **Video Report** → `tests/Result/video-reports/`  
    - 각 테스트 함수의 **실행 과정이 동영상으로 기록**됩니다.  
  - 🖼️ **Image Report** → `tests/Result/image/`  
    - 테스트 함수에서 인식한 이미지가 **기기 및 테스트 함수별 PNG 파일로 저장**됩니다.

### 4️⃣ **CI 환경 (Jenkins + AWS + 로컬 테스트 실행)**
- AWS EC2(Ubuntu)에 **Jenkins를 구축**하여 테스트를 원격 제어하도록 구성했습니다.  
- Jenkins는 **명령 제어 역할**을 수행하며,  
  특정 저장소의 변경사항이 webhook을 통해 감지되면  
  이를 기반으로 **별도 저장소의 테스트 코드를 사용해 Windows 로컬 환경에서 실제 테스트를 실행**합니다.  
- 로컬 PC에는 **Appium Server, Android Emulator, Pytest 환경**이 구성되어 있으며,  
  Jenkins에서 원격 명령으로 pytest를 실행해 테스트를 수행합니다.  
- 테스트 결과(HTML Report 및 동영상)는 로컬 환경의 `tests/Result/test-reports` 폴더에 자동 생성되며,  
  Jenkins 콘솔을 통해 테스트 진행 상황을 **실시간으로 확인**할 수 있습니다.

---

## ⚙️ Tech Stack
| 구분 | 사용 기술 |
|------|------------|
| Test Framework | **Pytest**, **Appium 3.0.2**, **uiautomator2** |
| Language | **Python 3.13.7** |
| CI/CD | **Jenkins (on AWS EC2, Ubuntu)** |
| Report | **pytest-html**, **Video Recording** |
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
│   └── (Testcase)The_App.xlsm                   # 테스트 시나리오별 테스트 케이스 문서
│
├── tests/                                       # 테스트 코드 및 결과 관리 폴더
│   ├── conftest.py                              # pytest 전역 설정 및 Appium driver fixture 정의
│   │
│   ├── common_util/                             # 공통 유틸리티 모듈
│   │   ├── control_image.py                     # SSIM 기반 이미지 유사도 검증 모듈
│   │
│   ├── image/                                   # baseline 이미지 저장 폴더
│   │   ├── original_1.png ~ original_6.png      # 비교 기준 이미지 파일들
│   │
│   ├── testcase/                                # 기능별 테스트 모듈
│   │   ├── test_0_app_start.py                  # 앱 실행 및 초기 화면 테스트
│   │   ├── test_1_echo_box.py                   # Echo Box 기능 검증
│   │   ├── test_2_login_screen.py               # 로그인 화면 검증
│   │   ├── test_4_webview_demo.py               # WebView 기능 검증
│   │   └── test_7_photo_demo.py                 # Photo Demo 기능 검증
│   │
│   ├── Results/                                 # 실제 테스트 결과 저장 폴더 (HTML Report, 영상, 캡처 포함)
│   │   ├── image/                               # 테스트 중 캡처 이미지 저장
│   │   │   ├── [device-1]/                      # 예: emulator-5554, localhost-5555 등
│   │   │   │   ├── [test_module]/               # 예: test_photo, test_image_text 등
│   │   │   │   │   ├── captured_1.png
│   │   │   │   │   ├── captured_2.png
│   │   │   │   │   └── ...
│   │   │   └── [device-2]/                      # 두 번째 테스트 기기 폴더
│   │   │       └── ...
│   │   │
│   │   ├── test-reports/                        # pytest HTML Report 저장 폴더
│   │   │   └── report_YYYY-MM-DD_HH-MM-SS.html  # 실행 시각 기준 자동 생성된 리포트 파일
│   │   │
│   │   └── video-reports/                       # 테스트 실행 중 녹화 영상 저장 폴더
│   │       ├── [device-1]/                      # 예: emulator-5554
│   │       │   ├── [test_case_name]/            # 예: test_0_app_start, test_login 등
│   │       │   │   ├── test_[scene]_01_YYYY-MM-DD_HH-MM-SS.mp4
│   │       │   │   ├── test_[scene]_02_YYYY-MM-DD_HH-MM-SS.mp4
│   │       │   │   └── ...
│   │       └── [device-2]/                      # 두 번째 테스트 기기 폴더
│   │           └── ...
│
├── requirements.txt                             # 테스트 환경 의존성 정의 파일
│
├── Jenkinsfile                                  # Jenkins Pipeline Groovy 스크립트
│
└── README.md                                    # 프로젝트 개요, 구조, 실행 방법 등 문서
```

---

## 🔐 Jenkins CI Server (on AWS)
| 항목 | 정보 |
|------|------|
| **Jenkins URL** | 🔗 [http://3.36.219.242:8080](http://3.36.219.242:8080) |
| **User ID** | `admin` |
| **Password** | `admin` |
| **Trigger** | GitHub Push 이벤트 기반 (테스트 전용 repo와 연동) |
| **Execution Flow** | Jenkins → Remote Windows (pytest 실행) → 로컬 환경에서 생성된 HTML Report 수집 → Jenkins에서 표시 |

📦 Jenkinsfile은 참고용으로 본 Repository 에도 포함되어 있으나, 실제 파이프라인은 트리거 역할을 하는 테스트 전용 저장소에서 실행됩니다.
두 저장소의 Jenkinsfile은 동일한 내용으로 작성되어 있습니다.

---

## ▶️ Run Locally

### 1️⃣ 환경 설정
```bash
# 필수 패키지 설치
pip install -r requirements.txt
```

### 2️⃣ 테스트 실행
```bash
# Pytest를 이용해 전체 테스트 실행
pytest -v

# (HTML Report 자동 생성)
결과 파일: tests/Result/test-reports/report_YYYY-MM-DD_HH-MM-SS.html
```

### 3️⃣ 개별 테스트 실행
```bash
# 특정 테스트 모듈만 실행 예시
pytest -v tests/testcase/test_2_login_screen.py
```

### 4️⃣ 결과 확인
- 📊 **HTML Report:** `tests/Result/test-reports/`  
- 🎥 **Video Report:** `tests/Result/video-reports/`  
- 🖼️ **Image:** `tests/Result/image/`

---

## 💡 Future Improvement
- iOS 환경 자동화 (Appium + XCUITest)  
- **Allure Report** 적용을 통한 테스트 결과 시각화 고도화
- 테스트 케이스 Excel 연동을 통한 결과 자동 업데이트

---

## 👩‍💻 Author
**이연정 (YJ)**  
QA Engineer  
📧 **asa48284828@gmail.com**
