@Library("Shared") _
pipeline {
    agent { label 'vinod' }

    environment {
        REPO_URL = 'https://github.com/dipdaiict/jenkins-cicd-learning.git'
        BRANCH = 'main'
        DOCKER_IMAGE = 'fastapi_test:latest'
        DOCKER_TAGGED_IMAGE = 'dippdatel/fastapi-jenkins:latest'
        CREDENTIALS_ID = 'DockerHubCreds'
    }

    stages {
        stage('Greet') {
            steps {
                hello()
            }
        }

        stage('Clone') {
            steps {
                gitClone(REPO_URL, BRANCH)
            }
        }

        stage('Build Docker Image') {
            steps {
                dockerBuild(DOCKER_IMAGE)
            }
        }

        stage('Test Container') {
            steps {
                sh '''
                    docker run -d -p 8000:8000 --name fastapi_test_container fastapi_test:latest
                    sleep 5
                    curl -f http://localhost:8000/health
                '''
            }
            post {
                always {
                    sh '''
                        docker stop fastapi_test_container || true
                        docker rm fastapi_test_container || true
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                dockerPush(DOCKER_IMAGE, DOCKER_TAGGED_IMAGE, CREDENTIALS_ID)
            }
        }

        stage('Success') {
            steps {
                echo 'Pipeline completed successfully.'
            }
        }
    }
}
