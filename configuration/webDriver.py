from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "uiautomator2"
options.device_name = "R3CX306FV2J"
options.app_package = "com.appiumpro.the_app"
options.app_activity = "com.appiumpro.the_app.MainActivity"
options.auto_grant_permissions = True
options.no_reset = True
# options.auto_webview = True  # 필요 시 활성화

appium_server_url = 'http://localhost:4723'

wd = webdriver.Remote('http://localhost:4723', options=options)

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