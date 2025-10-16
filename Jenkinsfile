pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "seguridad_contrasenas1:latest"
        KUBE_NAMESPACE = "myapp-namespace"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ferreirajuanpablo923-dot/nuevas.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Construyendo imagen Docker..."
                    sh 'docker build -t seguridad_contrasenas1:latest .'
                }
            }
        }

        stage('Push Docker Image (local)') {
            steps {
                script {
                    echo "Imagen construida localmente (sin push a registry)."
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Aplicando despliegue en Kubernetes..."
                    sh 'kubectl apply -f k8s/core-deployment.yaml -n myapp-namespace'
                }
            }
        }

        stage('Post-deploy check') {
            steps {
                script {
                    sh 'kubectl get pods -n myapp-namespace'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Despliegue completado exitosamente."
        }
        failure {
            echo "❌ Error durante el pipeline."
        }
    }
}
