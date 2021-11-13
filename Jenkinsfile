pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/melona2020/pythonproject.git']]])
            }
        }
        stage('Build') {
            steps {
                git 'https://github.com/melona2020/pythonproject.git'  
                sh 'python3 RandomPassGen.py'
            }
        }
        stage('Test') {
            steps {
                echo  'The Job has been tested'
            }
        }
    }
}
