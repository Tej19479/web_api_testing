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
                sh '''
                    cat read.me
                '''
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
