// Jenkinsfile.deploy - BUILD Job for Android APK (theapp_deploy)
// Agent: linux_02
// Purpose: Build Android APK and trigger test job

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
                    echo "Setting executable permissions for Android tools..."
                    chmod +x $ANDROID_HOME/platform-tools/* 2>/dev/null || true
                    chmod +x $ANDROID_HOME/build-tools/33.0.0/* 2>/dev/null || true
                    
                    echo "ADB version:"
                    adb --version
                '''
            }
        }
        
        stage('Build Debug APK') {
            steps {
                echo '🔨 Building Debug APK...'
                dir('android') {
                    sh '''
                        chmod +x ./gradlew
                        ./gradlew clean assembleDebug
                    '''
                }
            }
        }
        
        stage('Build Release APK') {
            steps {
                echo '🔨 Building Release APK...'
                dir('android') {
                    sh './gradlew assembleRelease'
                }
            }
        }
        
        stage('Verify APK Files') {
            steps {
                echo '📱 Verifying APK files...'
                sh '''
                    echo "Debug APK:"
                    ls -lh android/app/build/outputs/apk/debug/app-debug.apk
                    
                    echo ""
                    echo "Release APK:"
                    ls -lh android/app/build/outputs/apk/release/app-release.apk
                '''
            }
        }
        
        stage('Archive APK Artifacts') {
            steps {
                echo '📦 Archiving APK artifacts to Jenkins...'
                archiveArtifacts artifacts: 'android/app/build/outputs/apk/**/*.apk',
                                 fingerprint: true,
                                 allowEmptyArchive: false
            }
        }
        
        stage('Trigger Test Job') {
            steps {
                echo '🚀 Triggering theapp_test job on Windows agent...'
                build job: 'theapp_test',
                      parameters: [
                          string(name: 'APK_BUILD_NUMBER', value: "${env.BUILD_NUMBER}"),
                          string(name: 'APK_TYPE', value: 'release')
                      ],
                      wait: false
            }
        }
    }
    
    post {
        success {
            echo "✅ Build #${env.BUILD_NUMBER} completed successfully!"
            echo "📦 APK artifacts are stored in Jenkins"
            echo "🚀 Test job has been triggered"
        }
        failure {
            echo '❌ Build failed!'
            echo 'Check the console output for details'
        }
        cleanup {
            echo '🧹 Cleaning workspace...'
            cleanWs()
        }
    }
}