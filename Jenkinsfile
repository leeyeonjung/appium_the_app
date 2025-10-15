pipeline {
    agent { label 'windows' }   // ✅ Windows Agent에서 실행

    triggers {
        githubPush()            // ✅ GitHub Webhook으로 push 시 자동 실행
    }

    stages {
        stage('Checkout Test Code') {
            steps {
                echo "📦 Updating local appium_the_app repository..."
                bat '''
                cd C:\\appium_the_app
                git fetch origin main
                git reset --hard origin/main
                '''
            }
        }

        stage('Run Pytest on Windows') {
            steps {
                echo "🚀 Running tests on Windows..."
                bat '''
                cd C:\\appium_the_app
                pytest -v --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Collect Latest Report') {
            steps {
                echo "📊 Collecting latest HTML report..."
                bat '''
                REM ============================================
                REM 📊 최신 HTML 리포트 1개만 Jenkins로 복사
                REM ============================================

                setlocal enabledelayedexpansion

                REM 📁 HTML 리포트 폴더 (이모지 포함)
                set "REPORT_DIR=C:\\appium_the_app\\tests\\Result\\test-reports"

                REM 최신 HTML 파일 1개 찾기
                for /f "delims=" %%a in ('dir /b /a-d /o-d "!REPORT_DIR!\\*.html"') do (
                    set "LATEST=%%a"
                    goto found
                )
                :found

                if not defined LATEST (
                    echo ❌ No HTML report found in "!REPORT_DIR!"
                    exit /b 1
                )

                echo ✅ Found latest report: !LATEST!
                echo Copying to workspace...
                copy "!REPORT_DIR!\\!LATEST!" "%WORKSPACE%\\!LATEST!" >nul
                echo ✅ Copied "!LATEST!" to Jenkins workspace.

                endlocal
                '''
            }
        }
    }

    post {
        always {
            echo "📤 Archiving latest HTML report to Jenkins..."
            archiveArtifacts artifacts: '*.html', onlyIfSuccessful: false
        }
    }
}