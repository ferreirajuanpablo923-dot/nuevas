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
                bat 'echo Compilando proyecto...'
                // Ejemplo si usas Python:
                // bat 'python -m compileall .'
                // o Node:
                // bat 'npm install && npm run build'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                bat 'docker build -t seguridad_contrasenas1:latest .'
            }
        }

        stage('Publicar artefactos') {
            steps {
                bat 'mkdir artifacts'
                bat 'echo Build generado el %date% %time% > artifacts/info.txt'
                archiveArtifacts artifacts: 'artifacts/**/*', fingerprint: true
            }
        }

        stage('Desplegar en Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/ -n myapp-namespace'
            }
        }
    }

    post {
        success {
            echo '✅ Despliegue completado con éxito'
        }
        failure {
            echo '❌ Error en el pipeline'
        }
    }
}
