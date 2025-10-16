pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/ferreirajuanpablo923-dot/nuevas.git'
            }
        }

        stage('Construir proyecto') {
            steps {
                bat '''
                    echo Compilando proyecto...
                '''
            }
        }

        stage('Construir imagen Docker') {
            steps {
                bat '''
                    docker build -t seguridad_contrasenas1:latest .
                '''
            }
        }

        stage('Publicar artefactos') {
            steps {
                bat '''
                    if not exist artifacts mkdir artifacts
                    echo Build generado el %DATE% %TIME% > artifacts\\info.txt
                    dir artifacts
                    type artifacts\\info.txt
                '''
                archiveArtifacts artifacts: 'artifacts/**', fingerprint: true
            }
        }

        stage('Desplegar en Kubernetes') {
            when {
                expression { return false } // Temporal: salta esta etapa si no está configurado Kubernetes
            }
            steps {
                bat '''
                    kubectl apply -f k8s/ -n myapp-namespace
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completado exitosamente.'
        }
        failure {
            echo '❌ Error en el pipeline'
        }
    }
}
