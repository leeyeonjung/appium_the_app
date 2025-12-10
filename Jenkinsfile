// Jenkinsfile.deploy - BUILD Job for Android APK (theapp_deploy)
// Agent: linux_02
// Purpose: Build Debug APK → Test → Build Release APK

pipeline {
    agent { label 'linux_02' }
    
    environment {
        ANDROID_HOME = '/home/ubuntu/android-sdk'
        PATH = "${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/build-tools/33.0.0:${env.PATH}"
    }
    
    stages {
        stage('Checkout Android Project') {
            steps {
                echo '📥 Checking out Android project from GitHub...'
                checkout scm
            }
        }
        
        stage('Verify Environment') {
            steps {
                echo '🔍 Verifying build environment...'
                sh '''
                    echo "ANDROID_HOME: $ANDROID_HOME"
                    
                    echo "Java version:"
                    java -version
                    
                    echo ""
                    echo "Node.js version:"
                    node --version
                    
                    echo "npm version:"
                    npm --version
                    
                    echo ""
                    echo "Setting executable permissions for Android tools..."
                    chmod +x $ANDROID_HOME/platform-tools/* 2>/dev/null || true
                    chmod +x $ANDROID_HOME/build-tools/33.0.0/* 2>/dev/null || true
                    
                    echo "ADB version:"
                    adb --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '📦 Installing npm dependencies...'
                sh 'npm install'
            }
        }
        
        stage('Build Debug APK') {
            steps {
                echo '🔨 Building Debug APK for testing...'
                dir('android') {
                    sh '''
                        chmod +x ./gradlew
                        ./gradlew clean assembleDebug
                    '''
                }
            }
        }
        
        stage('Verify Debug APK') {
            steps {
                echo '📱 Verifying Debug APK...'
                sh '''
                    ls -lh android/app/build/outputs/apk/debug/app-debug.apk
                '''
            }
        }
        
        stage('Archive Debug APK') {
            steps {
                echo '📦 Archiving Debug APK for testing...'
                archiveArtifacts artifacts: 'android/app/build/outputs/apk/debug/app-debug.apk',
                                 fingerprint: true,
                                 allowEmptyArchive: false
            }
        }
        
        stage('Run Tests with Debug APK') {
            steps {
                echo '🧪 Triggering theapp_test with Debug APK...'
                script {
                    def testResult = build job: 'theapp_test',
                                           parameters: [
                                               string(name: 'APK_BUILD_NUMBER', value: "${env.BUILD_NUMBER}"),
                                               string(name: 'APK_TYPE', value: 'debug')
                                           ],
                                           wait: true,  // ⭐ 테스트 완료까지 대기
                                           propagate: true  // ⭐ 테스트 실패 시 이 job도 실패
                    
                    echo "✅ Tests passed with Debug APK!"
                }
            }
        }
        
        stage('Build Release APK') {
            steps {
                echo '🚀 Tests passed! Building Release APK...'
                dir('android') {
                    sh './gradlew assembleRelease'
                }
            }
        }
        
        stage('Verify Release APK') {
            steps {
                echo '📱 Verifying Release APK...'
                sh '''
                    ls -lh android/app/build/outputs/apk/release/app-release.apk
                    
                    echo ""
                    echo "APK Info:"
                    file android/app/build/outputs/apk/release/app-release.apk
                '''
            }
        }
        
        stage('Archive Release APK') {
            steps {
                echo '📦 Archiving Release APK (production-ready)...'
                archiveArtifacts artifacts: 'android/app/build/outputs/apk/release/app-release.apk',
                                 fingerprint: true,
                                 allowEmptyArchive: false
            }
        }
    }
    
    post {
        success {
            echo "✅ Build #${env.BUILD_NUMBER} completed successfully!"
            echo "🧪 Debug APK tested and passed"
            echo "📦 Release APK is ready for deployment"
        }
        failure {
            echo '❌ Build or tests failed!'
            echo 'Release APK was not created'
        }
        cleanup {
            echo '🧹 Cleaning workspace...'
            cleanWs()
        }
    }
}
