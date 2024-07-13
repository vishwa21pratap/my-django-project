pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-django-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the Git repository
                git url: 'https://github.com/vishwa21pratap/my-django-project.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests inside the Docker container
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Archive Results') {
            steps {
                // Archive test results
                junit 'test-reports/*.xml'
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
