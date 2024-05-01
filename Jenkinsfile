pipeline {
    agent any

    tools {
        // Define SonarQube scanner tool if it's not automatically detected
        sonarQube 'SonarQubeTool'
    }

    environment {
        // Define the project key, ideally this should be in your SonarQube project settings
        SONAR_PROJECT_KEY = 'download_file'
        SONAR_HOST_URL = 'http://your-sonarqube-server-url'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                script {
                    sh 'python -m pip install --user --upgrade pip'
                    sh 'pip install boto3 --user'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube scanner
                    withSonarQubeEnv('sonar') {
                        sh """
                           sonar-scanner \
                                -Dsonar.projectKey=download_file \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://54.146.65.235 \
                                -Dsonar.login=c1e01a2dc8fb3010c598d5b5d7b6732d95883571
                        """
                    }
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    sh 'python3 download_s3.py'
                }
            }
        }
    }
    post {
        always {
            // Notify or handle pipeline completion
            echo 'Check SonarQube for analysis details'
        }
    }
}

