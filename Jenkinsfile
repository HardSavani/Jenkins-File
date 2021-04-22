pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Compile') { 
            steps {
                sh 'python sample.py'
            }
        }
    }
}
