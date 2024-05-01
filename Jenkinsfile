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
                    // Assuming Python3 and pip are installed
                    sh 'python -m pip install --user --upgrade pip'
                    sh 'pip install boto3 --user'
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    sh 'python download_file_from_s3.py'
                }
            }
        }
    }
}
