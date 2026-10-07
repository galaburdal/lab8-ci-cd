pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_LOGIN/YOUR_REPO.git'
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh 'python3 -m pip install pylint --break-system-packages'
                sh 'pylint --disable=C,R,E0401,W0613 features/steps/'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run UI Tests') {
            steps {
                script {
                    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                        sh 'python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure-results'
                    }
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
