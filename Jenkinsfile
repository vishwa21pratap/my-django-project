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
                    def dockerImage = docker.build("my-django-app")
                    // Tag the Docker image
                    dockerImage.tag("my-django-app:${BUILD_NUMBER}")
                    dockerImage.tag("my-django-app:latest")
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
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
