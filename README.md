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
| Containerization | **Docker / Docker Compose** (Appium Server) |
| Report | **pytest-html**, 동영상 녹화 |
| Device | Android Emulator / Physical Device |

---

## 🏗️ Project Structure
```
appium_the_app/
├── app/
│   └── app-release.apk
├── appium_server/
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── testcase_excel/
│   └── (Testcase)The_App.xlsm
├── tests/
│   ├── conftest.py
│   ├── common_util/
│   │   ├── control_image.py
│   ├── image/
│   │   ├── original_1.png ~ original_6.png
│   ├── testcase/
│   │   ├── test_0_app_start.py
│   │   ├── test_1_echo_box.py
│   │   ├── test_2_login_screen.py
│   │   ├── test_4_webview_demo.py
│   │   └── test_7_photo_demo.py
│   ├── Results/
│   │   ├── image/
│   │   ├── test-reports/
│   │   └── video-reports/
├── requirements.txt
└── README.md
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
- AWS EC2 (Ubuntu)에 **Jenkins 서버를 구축**하여 테스트를 원격으로 제어하도록 구성  
- Jenkins는 **명령 제어 역할**을 수행하며, 실제 테스트는 **Windows 로컬 PC**에서 실행  
- 로컬 PC에는 **Appium Server, Android Emulator, Pytest 환경**이 상시 구동되어 있으며,  
  Jenkins에서 원격 명령으로 pytest를 실행하여 테스트를 수행  
- 테스트 결과(HTML Report 및 동영상)는 로컬 환경의 `tests/Result/` 폴더에 자동 생성  
- Jenkins 콘솔에서는 실행 로그를 통해 테스트 진행 상황을 실시간으로 확인 가능

---

## 🔐 Jenkins CI Server (on AWS)
| 항목 | 정보 |
|------|------|
| **Server OS** | Ubuntu 24.04 LTS (AWS EC2) |
| **Jenkins URL** | 🔗 [http://3.36.219.242:8080](http://3.36.219.242:8080) |
| **User ID** | `admin` |
| **Password** | `admin` |
| **Trigger** | GitHub Push 이벤트 기반 (테스트 전용 repo와 연동) |
| **Execution Flow** | Jenkins → Remote Windows (pytest 실행) → 로컬 환경에서 생성된 HTML Report 수집 → Jenkins 대시보드 표시 |

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
- 테스트 케이스 Excel 연동 통한 테력

---

## 👩‍💻 Author
**이연정 (YJ)**  
- QA Automation Engineer  
- 📧 Contact: asa48284828@gmail.com
