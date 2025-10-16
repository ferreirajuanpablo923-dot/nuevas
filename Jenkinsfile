pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "seguridad_contrasenas1:latest"
        KUBE_NAMESPACE = "myapp-namespace"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Clonando repositorio..."
                git branch: 'main', url: 'https://github.com/ferreirajuanpablo923-dot/nuevas.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Construyendo imagen Docker..."
                bat """
                docker build -t %DOCKER_IMAGE% .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Aplicando despliegue en Kubernetes..."
                bat """
                kubectl apply -f k8s/core-deployment.yaml -n %KUBE_NAMESPACE%
                """
            }
        }

        stage('Ver pods activos') {
            steps {
                bat """
                kubectl get pods -n %KUBE_NAMESPACE%
                """
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline ejecutado correctamente en Windows — Docker + K8s OK"
        }
        failure {
            echo "❌ Error en el pipeline (revisar pasos anteriores)."
        }
    }
}
