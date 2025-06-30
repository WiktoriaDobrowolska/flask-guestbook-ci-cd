pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Brak testów jednostkowych - aplikacja startowa."'
            }
        }
    }
}
