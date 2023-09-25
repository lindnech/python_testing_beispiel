pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'python3 ops.py'
            }
        }
        stage('Testing file') {
            steps {
                sh "python3 -m pytest"
            }
        }
        stage('Deliver') {
            steps {
                echo "Hi lindnec"
            }
        } 
    }
}
