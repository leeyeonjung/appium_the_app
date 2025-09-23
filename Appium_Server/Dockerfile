FROM node:18

# Appium 서버 설치 (버전 고정)
RUN npm install -g appium@3.0.2

# Appium uiautomator2 드라이버 설치 (버전 고정)
RUN appium driver install uiautomator2@5.0.1

# Appium 서버 실행 옵션
CMD ["appium", "--allow-insecure", "uiautomator2:chromedriver_autodownload", "--log-timestamp", "--relaxed-security"]
