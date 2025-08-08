pipeline {
    agent any
    environment{
     hellls="Python_path"
    }

    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'edge'],
            description: 'Select the browser to open'
        )

        string(
            name: 'TestingWebsiteURL',
            defaultValue: 'https://www.faircent.in/',
            description: 'Enter the testing URL.'
        )

        string(
            name: 'reportname',
            defaultValue: 'testing.html',
            description: 'Enter the report name.'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
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
                        sh 'cat README.md'
                    } else {
                        echo "Running on Windows..."
                        bat 'type README.md'
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

        stage('Branch Name Print') {
            steps {
                echo "Branch name is: ${env.BRANCH_NAME}"
            }
        }
       stage('Set up the environment for project') {
          steps {
                script {
                    echo "The Python path is: ${env.PATH}"  // Optional: show PATH if needed
                    bat 'python --version'
                }
         }
       }


       stage('Create Virtual Environment') {
                steps {
                    dir("${env.WORKSPACE}") {
                        script {
                            def venvName = "${env.JOB_NAME}".replaceAll("[^a-zA-Z0-9]", "_")  // Safe venv name
                            if (isUnix()) {
                                echo "Creating virtual environment on Unix with name: ${venvName}"
                                sh "python -m venv ${venvName}"
                            } else {
                                echo "Creating virtual environment on Windows with name: ${venvName}"
                                bat "python -m venv ${venvName}"
                            }
                        }
                    }
                }
       }

    }
}
