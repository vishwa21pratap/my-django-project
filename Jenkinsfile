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

        stage('Run Tests') {
            steps {
                script {
                    // Convert Windows path to Unix-style path
                    def workspaceUnix = pwd().replace('\\', '/')
                    echo "Unix-style workspace path: ${workspaceUnix}"
                    
                    // Run tests inside the Docker container
                    docker.image(DOCKER_IMAGE).inside("-v ${workspaceUnix}:/usr/src/app") {
                        sh 'ls -al /usr/src/app' // List files to check if the path is correct
                        sh 'python manage.py test'
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
