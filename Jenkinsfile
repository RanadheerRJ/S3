pipeline {
    agent any

    environment {
        // Define any environment variables here
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

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'The job was a success!'
        }
        failure {
            echo 'The job failed.'
        }
    }
}

