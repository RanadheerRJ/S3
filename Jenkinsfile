pipeline {
    agent any
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
}

