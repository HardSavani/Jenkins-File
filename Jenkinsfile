pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'python'
            }
        }
        stage('Compile') { 
            steps {
                sh 'python sample.py'
            }
        }
    }
}
