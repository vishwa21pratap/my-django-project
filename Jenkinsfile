pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vishwa21pratap/my-django-project.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-django-app")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    def workspacePath = pwd()
                    echo "Unix-style workspace path: ${workspacePath}"
                    docker.image("my-django-app").inside {
                        sh 'pytest'
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
