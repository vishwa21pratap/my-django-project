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
                    def dockerImage = docker.build("my_django_app")
                    // Tag the Docker image
                    dockerImage.tag("my_django_app:${BUILD_NUMBER}")
                    dockerImage.tag("my_django_app:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("my_django_app").inside('-v /var/run/docker.sock:/var/run/docker.sock') {
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
