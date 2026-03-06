pipeline {

    agent any

    stages {

        stage('Clone Repo') {
	    steps {
                git 'https://github.com/Spoorthisgowda20s/ai-devops-project.git'
    }
}

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-sales-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:8081 ai-sales-app'
            }
        }

    }
}