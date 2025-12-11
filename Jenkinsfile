// Jenkinsfile.deploy - BUILD Job for Android APK (theapp_deploy)
// Agent: linux_02
// Purpose: Build Release APK → Test → Archive

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
                    java -version
                    node --version
                    chmod +x $ANDROID_HOME/platform-tools/* 2>/dev/null || true
                    chmod +x $ANDROID_HOME/build-tools/33.0.0/* 2>/dev/null || true
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo '📦 Installing npm dependencies...'
                sh 'npm install'
            }
        }
        
        stage('Build Release APK') {
            steps {
                echo '🔨 Building Release APK...'
                dir('android') {
                    sh '''
                        chmod +x ./gradlew
                        ./gradlew clean assembleRelease
                    '''
                }
            }
        }
        
        stage('Verify Release APK') {
            steps {
                echo '📱 Verifying Release APK...'
                sh 'ls -lh android/app/build/outputs/apk/release/app-release.apk'
            }
        }
        
        stage('Archive APK for Testing') {
            steps {
                echo '📦 Archiving Release APK...'
                archiveArtifacts artifacts: 'android/app/build/outputs/apk/release/app-release.apk',
                                 fingerprint: true,
                                 allowEmptyArchive: false
            }
        }
        
        stage('Run Tests with Release APK') {
            steps {
                echo '🧪 Running Appium tests...'
                script {
                    def testResult = build job: 'theapp_test',
                                           parameters: [
                                               string(name: 'APK_BUILD_NUMBER', value: "${env.BUILD_NUMBER}"),
                                               string(name: 'APK_TYPE', value: 'release')
                                           ],
                                           wait: true,
                                           propagate: true
                    
                    echo "✅ Tests passed! Report: ${env.JENKINS_URL}job/theapp_test/${testResult.number}/"
                }
            }
        }
    }
    
    post {
        success {
            echo "✅ Build #${env.BUILD_NUMBER} completed! Release APK is ready for deployment"
        }
        failure {
            echo '❌ Build or tests failed! Check console output for details'
        }
        cleanup {
            cleanWs()
        }
    }
}
 