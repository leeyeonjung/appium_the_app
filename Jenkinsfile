pipeline {
    agent { label 'windows' }

    triggers {
        githubPush()   // ✅ GitHub webhook push 시 자동 실행
    }

    stages {

        stage('Skip Info') {
            when {
                not { changeset pattern: "jenkins_test_repo/**", comparator: "ANT" }
            }
            steps {
                echo "🟡 No changes in jenkins_test_repo → Skipping test execution."
                script {
                    // ✅ 변경 없을 경우 파이프라인 즉시 종료
                    currentBuild.result = 'SUCCESS'
                    echo "🛑 Pipeline stopped: No test changes detected."
                    error("Stop remaining stages due to no changes.")
                }
            }
        }

        stage('Checkout Test Code') {
            when {
                changeset pattern: "jenkins_test_repo/**", comparator: "ANT"
            }
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
            when {
                changeset pattern: "jenkins_test_repo/**", comparator: "ANT"
            }
            steps {
                echo "🚀 Detected changes in jenkins_test_repo → Running tests..."
                // ⚠️ pytest 실패해도 이후 단계 계속 진행
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat '''
                        cd C:\\appium_the_app
                        pytest -v --maxfail=1 --disable-warnings
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "📊 Collecting latest HTML report (always, even if failed)..."
            bat '''
                REM ============================================
                REM 📊 최신 HTML 리포트 1개만 Jenkins로 복사
                REM ============================================

                setlocal enabledelayedexpansion
                set "REPORT_DIR=C:\\appium_the_app\\tests\\Result\\test-reports"
                set "LATEST="

                for /f "delims=" %%A in ('dir /b /a-d /o-d "%REPORT_DIR%\\*.html"') do (
                    set "LATEST=%%A"
                    goto :found
                )

                :found
                if not defined LATEST (
                    echo ❌ No HTML report found in "%REPORT_DIR%"
                    exit /b 1
                )

                echo ✅ Found latest report: !LATEST!
                copy "%REPORT_DIR%\\!LATEST!" "%WORKSPACE%\\!LATEST!" >nul
                echo ✅ Copied !LATEST! to Jenkins workspace.
                endlocal
            '''

            echo "📤 Archiving latest HTML report to Jenkins..."
            archiveArtifacts artifacts: '*.html', onlyIfSuccessful: false

            // ✅ HTML Publisher Plugin - Jenkins 탭에 바로 표시
            publishHTML(target: [
                reportName: '📈 Appium Test Report',
                reportDir: '.',
                reportFiles: '*.html',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: false
            ])
        }
    }
}
