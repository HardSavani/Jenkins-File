pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install python3.7.4'
            }
        }
        stage('Compile') { 
            steps {
                sh 'python sample.py'
            }
        }
    }
}
