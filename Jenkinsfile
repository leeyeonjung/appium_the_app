// Jenkinsfile - TEST Job for Appium Tests (theapp_test)
// Agent: windows_01
// Purpose: Run Appium automated tests on Android device

pipeline {
    agent { label 'windows_01' }
    
    parameters {
        string(name: 'APK_BUILD_NUMBER', defaultValue: 'latest', description: 'APK Build Number from theapp_deploy')
        choice(name: 'APK_TYPE', choices: ['release', 'debug'], description: 'APK Type to test')
    }
    
    environment {
        // Map ANDROID_DEVICES to DEVICES for conftest.py
        DEVICES = "${env.ANDROID_DEVICES}"
        APPIUM_SERVICE = 'AppiumServer1'
        APPIUM_PORT = '4723'
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout Test Code') {
            steps {
                echo '📥 Checking out test code from GitHub...'
                checkout scm  // SCM 설정 그대로 사용 (더 간단!)
            }
        }
        
        stage('Setup Python Virtual Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                bat '''
                    if exist %VENV_DIR% rmdir /s /q %VENV_DIR%
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate && python -m pip install --upgrade pip
                    call %VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt
                '''
            }
        }
        
        stage('Verify Environment') {
            steps {
                echo '🔍 Verifying test environment...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    echo DEVICES Configuration:
                    echo %DEVICES%
                    echo.
                    echo Python version:
                    python --version
                    echo.
                    echo Installed packages:
                    pip list
                    echo.
                    echo ADB version:
                    adb --version
                '''
            }
        }
        
        stage('Copy APK from Build Job') {
            steps {
                echo "📦 Copying ${params.APK_TYPE} APK from theapp_deploy #${params.APK_BUILD_NUMBER}..."
                script {
                    bat 'if not exist app mkdir app'
                    
                    copyArtifacts projectName: 'theapp_deploy',
                                  selector: specific(params.APK_BUILD_NUMBER),
                                  filter: "android/app/build/outputs/apk/${params.APK_TYPE}/app-${params.APK_TYPE}.apk",
                                  target: 'app/',
                                  flatten: true
                }
                
                bat '''
                    echo 📱 APK file copied:
                    dir /B app\\*.apk
                '''
            }
        }
        
        stage('Check Connected Devices') {
            steps {
                echo '📱 Checking connected Android devices...'
                bat '''
                    echo Connected devices:
                    adb devices -l
                    
                    echo.
                    echo Device information:
                    adb shell getprop ro.product.model
                    adb shell getprop ro.build.version.release
                '''
            }
        }
        
        stage('Install APK on Device') {
            steps {
                echo '📲 Installing APK on device...'
                bat """
                    echo Uninstalling previous version (if exists)...
                    adb uninstall com.appiumpro.the_app 2>nul || echo No previous installation found
                    
                    echo.
                    echo Installing app-${params.APK_TYPE}.apk...
                    adb install -r app\\app-${params.APK_TYPE}.apk
                    
                    echo.
                    echo Verifying installation...
                    adb shell pm list packages | findstr appiumpro
                """
            }
        }
        
        stage('Start Appium Server') {
            steps {
                echo '🚀 Starting Appium Server (AppiumServer1)...'
                bat """
                    echo Checking service status...
                    sc query ${APPIUM_SERVICE}
                    
                    echo.
                    echo Starting Appium service...
                    net start ${APPIUM_SERVICE}
                    
                    echo.
                    echo Waiting for Appium to be ready...
                    timeout /t 5 /nobreak
                    
                    echo.
                    echo Verifying Appium is running on port ${APPIUM_PORT}...
                    netstat -ano | findstr :${APPIUM_PORT}
                """
            }
        }
        
        stage('Run Appium Tests') {
            steps {
                echo '🧪 Running Appium automated tests with pytest...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pytest -v --tb=short
                '''
            }
        }
        
        stage('Collect Test Results') {
            steps {
                echo '📊 Collecting test results...'
                script {
                    bat '''
                        if exist Result\\test-reports\\*.html (
                            echo ✅ HTML Test Reports found:
                            dir /B Result\\test-reports\\*.html
                            
                            echo.
                            echo 📝 Finding latest HTML report...
                            for /f "delims=" %%A in ('dir /b /o-d Result\\test-reports\\*.html 2^>nul') do (
                                set "LATEST_HTML=%%A"
                                goto :found
                            )
                            :found
                            if defined LATEST_HTML (
                                echo Latest report: %LATEST_HTML%
                                copy "Result\\test-reports\\%LATEST_HTML%" "windows_%LATEST_HTML%"
                                echo Renamed to: windows_%LATEST_HTML%
                            )
                        ) else (
                            echo ⚠️ No HTML reports found
                        )
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo '📦 Archiving test artifacts...'
            
            // Archive latest HTML test report (renamed with windows_ prefix)
            archiveArtifacts artifacts: 'windows_*.html',
                             allowEmptyArchive: true,
                             fingerprint: true
            
            echo '🛑 Stopping Appium Server...'
            bat """
                net stop ${APPIUM_SERVICE} 2>nul || echo Appium service already stopped
            """
            
            echo '📱 Uninstalling test APK from device...'
            bat '''
                adb uninstall com.appiumpro.the_app 2>nul || echo App already uninstalled
            '''
        }
        success {
            echo '✅ All tests passed successfully!'
            echo "📊 Test reports are available in Build #${env.BUILD_NUMBER} artifacts"
        }
        failure {
            echo '❌ Tests failed!'
            echo 'Check the console output and test reports for details'
            bat '''
                if exist appium.log (
                    echo.
                    echo === Appium Log ===
                    type appium.log
                )
            '''
        }
        cleanup {
            echo '🧹 Cleanup completed'
        }
    }
}
