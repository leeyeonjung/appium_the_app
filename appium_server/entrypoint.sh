#!/bin/bash
set -e

# Appium 홈 경로
export APPIUM_HOME=/root/.appium
mkdir -p "$APPIUM_HOME" /logs
chmod -R 777 /logs || true

# 드라이버 설치 체크 함수
has_uiautomator2 () {
  # 1) 실제 드라이버 폴더 존재 여부 확인
  if [ -d "/root/.appium/node_modules/appium-uiautomator2-driver" ]; then return 0; fi
  if [ -d "/home/androidusr/.appium/node_modules/appium-uiautomator2-driver" ]; then return 0; fi
  if [ -d "$APPIUM_HOME/node_modules/appium-uiautomator2-driver" ]; then return 0; fi

  # 2) CLI 리스트(색상/기호 제거 후 대소문자 무시)
  if appium driver list --installed 2>/dev/null \
      | sed -r 's/\x1B\[[0-9;]*[mK]//g' \
      | tr -d '\r' \
      | tr '[:upper:]' '[:lower:]' \
      | grep -q "uiautomator2"; then
    return 0
  fi

  return 1
}

# uiautomator2 설치 여부 확인
echo "[INFO] Checking 'uiautomator2' driver..."
if has_uiautomator2; then
  echo "[INFO] 'uiautomator2' is already installed. Skipping installation."
else
  echo "[INFO] 'uiautomator2' not found. Installing..."
  if ! appium driver install uiautomator2 >/tmp/u2_install.log 2>&1; then
    echo "[WARN] Install command reported a non-zero exit. This may still be okay if another APP_HOME had it."
    if has_uiautomator2; then
      echo "[INFO] Verified after install attempt: 'uiautomator2' present. Continuing."
    else
      echo "[ERROR] 'uiautomator2' still not found after install attempt. Showing last 40 lines:"
      tail -n 40 /tmp/u2_install.log || true
    fi
  fi
fi


# ====================== 실제 Appium 실행 ====================== #
# 날짜별 로그 생성
# 자정에 로그 날짜 변경되고, 7일지난 로그 삭제
while true; do
  TODAY=$(date +%Y-%m-%d)
  LOGFILE="/logs/appium_${TODAY}.log"

  echo "[INFO] Starting Appium at $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$LOGFILE"
  echo "[INFO] Logging (append mode) to $LOGFILE" | tee -a "$LOGFILE"

  # 7일 지난 로그 삭제
  find /logs -type f -name "appium_*.log" -mtime +7 -print -delete | tee -a "$LOGFILE" || true

  # Appium 서버 실행
  appium -p 4723 \
    --session-override \
    --log-timestamp \
    --relaxed-security \
    --allow-insecure uiautomator2,chromedriver_autodownload \
    --log-level info \
    --log "$LOGFILE" >> "$LOGFILE" 2>&1 &

  APP_PID=$!

  # 자정까지 남은 시간 계산
  NOW=$(date +%s)
  TOMORROW=$(date -d "tomorrow 00:00:00" +%s)
  SECONDS_UNTIL_MIDNIGHT=$((TOMORROW - NOW))
  if [ $SECONDS_UNTIL_MIDNIGHT -lt 1 ]; then
    SECONDS_UNTIL_MIDNIGHT=1
  fi
  echo "[INFO] Will rotate log at midnight (in $SECONDS_UNTIL_MIDNIGHT seconds)" | tee -a "$LOGFILE"

  sleep $SECONDS_UNTIL_MIDNIGHT

  echo "[INFO] Rotating log... Stopping Appium process $APP_PID" | tee -a "$LOGFILE"
  kill $APP_PID || true

  sleep 5
done