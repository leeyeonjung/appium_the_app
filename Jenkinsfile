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
                // ✅ Skip(ABORTED) 상태면 post 블록 실행하지 않음
                if (currentBuild.result == 'ABORTED') {
                    echo "⏩ Post block skipped (build was aborted)."
                    return
                }

                echo "📊 Collecting latest HTML report..."

                // ✅ 최신 HTML 1개만 Jenkins 워크스페이스로 복사 (파일명 변경 없음)
                bat '''
                    setlocal enabledelayedexpansion
                    set "REPORT_DIR=C:\\appium_the_app\\tests\\Result\\test-reports"
                    set "LATEST="

                    if not exist "%REPORT_DIR%" (
                        echo ⚠️ Report directory not found: "%REPORT_DIR%"
                        exit /b 0
                    )

                    REM 최신순으로 정렬 후 첫 번째(가장 최근) 파일만 선택
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

                echo "📤 Archiving only the latest HTML report..."
                archiveArtifacts artifacts: '*.html', fingerprint: true, onlyIfSuccessful: false
            }
        }
    }
}
