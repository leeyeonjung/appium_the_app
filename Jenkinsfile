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
                    // ✅ 파이프라인 중단 (이후 stage 및 post 실행 안 함)
                    currentBuild.result = 'ABORTED'
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
                // ⚠️ pytest 실패해도 파이프라인 계속 진행
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
            script {
                // ✅ Skip(ABORTED) 상태면 post 블록 내용 실행 안 함
                if (currentBuild.result == 'ABORTED') {
                    echo "⏩ Post block skipped (build was aborted)."
                    return
                }

                echo "📊 Collecting latest HTML report (always, even if failed)..."

                bat '''
                    REM ============================================
                    REM 📊 최신 HTML 리포트 1개만 Jenkins로 복사
                    REM ============================================

                    setlocal enabledelayedexpansion
                    set "REPORT_DIR=C:\\appium_the_app\\tests\\Result\\test-reports"
                    set "LATEST="

                    if not exist "%REPORT_DIR%" (
                        echo ⚠️ Report directory not found: "%REPORT_DIR%"
                        exit /b 0
                    )

                    for /f "delims=" %%A in ('dir /b /a-d /o-d "%REPORT_DIR%\\*.html" 2^>nul') do (
                        set "LATEST=%%A"
                        goto :found
                    )

                    :found
                    if not defined LATEST (
                        echo ⚠️ No HTML report found in "%REPORT_DIR%"
                        exit /b 0
                    )

                    echo ✅ Found latest report: !LATEST!
                    copy "%REPORT_DIR%\\!LATEST!" "%WORKSPACE%\\!LATEST!" >nul
                    echo ✅ Copied !LATEST! to Jenkins workspace.
                    endlocal
                '''

                echo "📤 Archiving latest HTML report to Jenkins..."
                archiveArtifacts artifacts: '*.html', onlyIfSuccessful: false
            }
        }
    }
}
