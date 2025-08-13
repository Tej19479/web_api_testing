pipeline {
    agent any
    environment {
        Python_path = "${env.Python_path}"
        PATH = "${Python_path};${env.PATH}"
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
                dir("${WORKSPACE}") {
                    bat '''
                        echo Current PATH:
                        echo %PATH%
                        echo This is Python path: %Python_path%

                        echo Checking Python version...
                        python --version
                    '''
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                dir("${env.WORKSPACE}") {
                    script {
                        venvName = "${env.JOB_NAME}".replaceAll("[^a-zA-Z0-9]", "_")
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

        stage('Activate Virtual Environment') {
            steps {
                dir("${WORKSPACE}") {
                    script {
                        if (isUnix()) {
                            sh "source ${venvName}/bin/activate && python --version"
                        } else {
                            bat """
                            call ${venvName}\\Scripts\\activate
                            python --version
                            echo Version check completed.
                            python -m pip install --upgrade pip
                             pip install -r requirements.txt || echo "No requirements.txt found"
                            echo Version check requement txt file.
                            """
                        }
                    }
                }
            }
        }

        stage('Run Testcases') {
            steps {
                dir("${WORKSPACE}") {
                    bat """
                        call ${venvName}\\Scripts\\activate
                        pytest -v -s tests/test_add_cart_item.py --html=reports/${BUILD_NUMBER}.html --self-contained-html
                    """
                }
            }
        }
    }
}
