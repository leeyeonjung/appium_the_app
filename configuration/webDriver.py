from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options

capabilities = {
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "R3CX306FV2J",
  "appium:appPackage": "com.appiumpro.the_app",
  "appium:appActivity": "com.appiumpro.the_app.MainActivity",
  "appium:autoGrantPermissions": "true", #권한 전체 자동 허용
  "appium:noreset": "true" #App data no reset
  # "autoWebview": "true" #자동 웹뷰 열기
}

appium_server_url = 'http://localhost:4723'

wd = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

def cal():
  wd.implicitly_wait(5)
  return wd

def xpath(data):
  return wd.find_element(By.XPATH, data)

def id(data):
  return wd.find_element(By.ID, data)

    
#webDriver.wd.close_app() / 앱 종료
#webDriver.wd.launch_app() / 앱 백그라운드에서 재시작
#webDriver.wd.reset() 
# ['NATIVE_APP', 'WEBVIEW_kr.co.nicevan.bujaapp']