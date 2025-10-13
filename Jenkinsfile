pipeline {
    agent { label 'windows' }

    triggers {
        // ✅ GitHub Webhook으로 push 이벤트 감지
        githubPush()
    }

    stages {
        stage('Checkout Test Code') {
            steps {
                echo "📦 Checking out appium_the_app repository..."
                git branch: 'main',
                    url: 'https://github.com/leeyeonjung/appium_the_app.git'
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
                set "REPORT_DIR=C:\\appium_the_app\\tests\\Result\\📊test-reports📊"
                for /f "delims=" %%a in ('dir /b /a-d /o-d "%REPORT_DIR%\\*.html"') do (
                    copy "%REPORT_DIR%\\%%a" "%WORKSPACE%\\latest_report.html"
                    goto done
                )
                :done
                '''
            }
        }
    }

    post {
        always {
            echo "📤 Archiving latest HTML report to Jenkins..."
            archiveArtifacts artifacts: 'latest_report.html', onlyIfSuccessful: false
        }
    }
}