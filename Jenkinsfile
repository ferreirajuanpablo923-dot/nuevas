pipeline {
    agent any

    environment {
        APP_NAME = "seguridad_app_${BUILD_NUMBER}" // nombre único para evitar conflictos
        IMAGE_NAME = "seguridad_contrasenas:latest"
    }

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
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Container') {
            steps {
                echo '🚀 Iniciando contenedor...'
                sh "docker rm -f ${APP_NAME} || true"  // elimina contenedor viejo si existe
                sh "docker run -d --name ${APP_NAME} -p 5000:5000 ${IMAGE_NAME}"
                sh "sleep 5"
            }
        }

        stage('Test E2E') {
            steps {
                echo '🧪 Ejecutando pruebas E2E dentro del contenedor...'
                sh "docker exec ${APP_NAME} python test_full_flow_e2e.py"
            }
        }

        stage('Cleanup') {
            steps {
                echo '🧹 Limpiando contenedores...'
                sh "docker stop ${APP_NAME} || true"
                sh "docker rm ${APP_NAME} || true"
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
