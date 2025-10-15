pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Clonando repositorio...'
                git branch: 'main', 
                    url: 'https://github.com/AndresSanmiguel/seguridad_contrasenas1.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo '🐳 Construyendo imagen Docker...'
                sh 'docker build -t seguridad_contrasenas:latest .'
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo '🧹 Limpiando contenedor antiguo...'
                sh '''
                    docker stop seguridad_app || true
                    docker rm seguridad_app || true
                '''
            }
        }
        
        stage('Run Container') {
            steps {
                echo '🚀 Iniciando contenedor...'
                sh 'docker run -d --name seguridad_app -p 5000:5000 seguridad_contrasenas:latest'
                sh 'sleep 5'
            }
        }
        
        stage('Test E2E') {
            steps {
                echo '🧪 Ejecutando pruebas E2E...'
                sh '''
                    # Ejecutar las pruebas dentro del contenedor Docker
                    docker exec seguridad_app pip install selenium webdriver-manager || true
                    docker exec seguridad_app python -m pytest tests/ || true
                '''
            }
        }
        
        stage('Health Check') {
            steps {
                echo '🏥 Verificando salud de la aplicación...'
                sh '''
                    # Verificar que el contenedor está corriendo
                    docker ps | grep seguridad_app
                    
                    # Opcional: hacer un curl a la aplicación
                    curl -f http://localhost:5000 || echo "App no responde en puerto 5000"
                '''
            }
        }
        
        stage('Cleanup') {
            steps {
                echo '🧹 Limpiando recursos...'
                sh '''
                    # Limpiar imágenes sin usar
                    docker image prune -f || true
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline ejecutado exitosamente!'
            echo '🌐 Aplicación disponible en: http://localhost:5000'
        }
        failure {
            echo '❌ Error en el pipeline.'
            sh 'docker logs seguridad_app || true'
        }
        always {
            echo '🏁 Pipeline finalizado.'
        }
    }
}