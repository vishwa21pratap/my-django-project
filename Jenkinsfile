pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-django-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the Git repository
                git url: 'https://github.com/vishwa21pratap/my-django-project.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build(DOCKER_IMAGE, "-f Dockerfile .")
                }
            }
        }

        
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
