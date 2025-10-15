pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Clonando repositorio...'
                git branch: 'main', url: 'https://github.com/AndresSanmiguel/seguridad_contrasenas1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Construyendo imagen Docker...'
                sh 'docker build -t seguridad_contrasenas:latest .'
            }
        }

        stage('Run Container') {
            steps {
                echo '🚀 Iniciando contenedor...'
                sh 'docker rm -f seguridad_app || true'
                sh 'docker run -d --name seguridad_app -p 5000:5000 seguridad_contrasenas:latest'
                sh 'sleep 5'
            }
        }

        stage('Test E2E') {
            steps {
                echo '🧪 Ejecutando pruebas E2E dentro del contenedor...'
                sh 'docker exec seguridad_app python test_full_flow_e2e.py'
            }
        }

        stage('Cleanup') {
            steps {
                echo '🧹 Limpiando contenedores...'
                sh 'docker stop seguridad_app || true'
                sh 'docker rm seguridad_app || true'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ejecutado correctamente.'
        }
        failure {
            echo '❌ Error en el pipeline.'
        }
    }
}
