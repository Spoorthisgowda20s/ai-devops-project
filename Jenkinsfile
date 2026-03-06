pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Spoorthisgowda20s/ai-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker-compose up -d'
            }
        }

    }
}
