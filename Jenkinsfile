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
                script {
                    // Crear directorio de artifacts
                    bat '''
                        if not exist artifacts mkdir artifacts
                        echo Build generado el %DATE% %TIME% > artifacts\\info.txt
                        echo Versión: Build #%BUILD_NUMBER% >> artifacts\\info.txt
                        echo Proyecto: seguridad_contrasenas1 >> artifacts\\info.txt
                        dir artifacts
                        type artifacts\\info.txt
                    '''
                    
                    // Copiar archivos importantes al directorio de artifacts
                    bat '''
                        copy Dockerfile artifacts\\Dockerfile.backup 2>nul || echo No hay Dockerfile
                        copy *.py artifacts\\ 2>nul || echo No hay archivos Python
                        copy *.html artifacts\\ 2>nul || echo No hay archivos HTML
                        dir artifacts
                    '''
                }
                
                // Archivar con patrón más específico
                archiveArtifacts artifacts: 'artifacts/*', 
                               fingerprint: true, 
                               allowEmptyArchive: false,
                               onlyIfSuccessful: false
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
            echo "📦 Artifacts archivados en Build #${env.BUILD_NUMBER}"
        }
        failure {
            echo '❌ Error en el pipeline'
        }
        always {
            // Verificar qué se archivó
            script {
                bat 'if exist artifacts dir artifacts'
            }
        }
    }
}