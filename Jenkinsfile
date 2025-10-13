pipeline {
    agent { label 'windows' }

    stages {
        stage('Run Pytest') {
            steps {
                bat '''
                    cd C:\\appium_the_app
                    pytest -v --disable-warnings
                '''
            }
        }
    }

    post {
        always {
            // 🔍 최신 HTML 리포트 찾기
            script {
                // PowerShell로 가장 최근 HTML 파일 경로 가져오기
                def latestReport = bat(
                    script: '''
                        $folder = "C:\\appium_the_app\\tests\\Result\\📊test-reports📊"
                        $latest = Get-ChildItem -Path $folder -Filter *.html | Sort-Object LastWriteTime -Descending | Select-Object -First 1
                        Write-Host $latest.FullName
                    ''',
                    returnStdout: true
                ).trim()

                // Jenkins용 경로 변환 (역슬래시 → 슬래시)
                latestReport = latestReport.replace("\\", "/")

                echo "📄 Latest HTML report: ${latestReport}"

                // reportDir / reportFiles 분리
                def reportDir  = latestReport.substring(0, latestReport.lastIndexOf("/"))
                def reportFile = latestReport.substring(latestReport.lastIndexOf("/") + 1)

                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: reportDir,
                    reportFiles: reportFile,
                    reportName: 'Latest Pytest Report'
                ])
            }
        }
    }
}