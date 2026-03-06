pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/YOURUSERNAME/ai-devops-project.git'
            }
        }

        stage('Build App') {
            steps {
                dir('aiapp') {
                    bat 'mvn clean package'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('aiapp') {
                    bat 'docker build -t aiapp .'
                }
            }
        }

        stage('Run DEV Container') {
            steps {
                bat 'docker run -d -p 8081:8080 -e ENV=DEV aiapp'
            }
        }

        stage('Run TEST Container') {
            steps {
                bat 'docker run -d -p 8082:8080 -e ENV=TEST aiapp'
            }
        }

        stage('Run PROD Container') {
            steps {
                bat 'docker run -d -p 8083:8080 -e ENV=PROD aiapp'
            }
        }

    }
}