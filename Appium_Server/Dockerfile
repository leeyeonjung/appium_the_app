FROM node:18

# adb 설치
RUN apt-get update && apt-get install -y android-tools-adb && rm -rf /var/lib/apt/lists/*

# 로그 디렉토리
RUN mkdir -p /logs

# Appium 서버 설치 (버전 고정)
RUN npm install -g appium@3.0.2

# Appium uiautomator2 드라이버 설치 (버전 고정)
RUN appium driver install uiautomator2@5.0.1

# 기본 포트
EXPOSE 4723

# === 컨테이너 시작 시 실행될 명령어 ===
# 날짜별 로그 파일 생성 + adb 초기화 + appium 실행
CMD LOGDATE=$(date +"%Y-%m-%d") && \
    adb kill-server && adb start-server && \
    exec appium \
      --allow-insecure uiautomator2:chromedriver_autodownload \
      --log-timestamp \
      --relaxed-security \
      > /logs/appium_${LOGDATE}.log 2>&1
