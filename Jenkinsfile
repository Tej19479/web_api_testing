pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }

        stage('Deploy Extra') {
            steps {
                echo 'Deploying additional application logic...'
            }
        }

        stage('Branch Pull for Fix Any Bugs') {
            when {
                branch pattern: "fix.*", comparator: "REGEXP"
            }
            steps {
                script {
                    if (isUnix()) {
                        echo "Running on Unix..."
                        sh 'cat README.me'
                    } else {
                        echo "Running on Windows..."
                        bat 'type README.md'
                        echo "tejjjjj"
                        echo "tehhehehe"
                    }
                }
            }
        }

        stage('For the PR - Pull Request') {
            when {
                branch pattern: "PR-.*", comparator: "REGEXP"
            }
            steps {
                echo 'This stage runs only for PR branches.'
            }
        }
    }
}
