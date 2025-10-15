pipeline {
    agent any

    environment {
        IMAGE_NAME = "seguridad_contrasenas"
        IMAGE_TAG = "latest"
    }

    stages {
      

        stage('Build Docker') {
            steps {
                script {
                    echo "🏗️ Construyendo imagen Docker..."
                    sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "🧪 Ejecutando pruebas E2E con Selenium..."
                    sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python test_full_flow_e2e.py'
                }
            }
        }

        stage('Push Image') {
            when {
                expression { return env.BRANCH_NAME == 'main' }
            }
            steps {
                script {
                    echo "📦 Subiendo imagen a Docker Hub..."
                    // Asegúrate de haber configurado tus credenciales en Jenkins (DockerHub)
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker tag ${IMAGE_NAME}:${IMAGE_TAG} $DOCKER_USER/${IMAGE_NAME}:${IMAGE_TAG}
                            docker push $DOCKER_USER/${IMAGE_NAME}:${IMAGE_TAG}
                        '''
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "🚀 Desplegando contenedor actualizado..."
                    sh '''
                        docker stop seguridad_app || true
                        docker rm seguridad_app || true
                        docker run -d --name seguridad_app -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completado con éxito.'
        }
        failure {
            echo '❌ Hubo un error en el pipeline.'
        }
    }
}
