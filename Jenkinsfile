pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build -t seguridad_contrasenas:${GIT_COMMIT} .'
      }
    }
    stage('Run Tests') {
      steps {
        sh 'docker run --rm seguridad_contrasenas:${GIT_COMMIT} python -m pytest tests || true'
      }
    }
    stage('Push Image') {
      when { branch 'main' }
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh 'echo $PASS | docker login -u $USER --password-stdin'
          sh 'docker tag seguridad_contrasenas:${GIT_COMMIT} tuusuario/seguridad_contrasenas:latest'
          sh 'docker push tuusuario/seguridad_contrasenas:latest'
        }
      }
    }
    stage('Deploy to AWS') {
      when { branch 'main' }
      steps {
        // Puedes usar CLI de AWS para desplegar en ECS/EB/EC2
        sh 'echo "Desplegar a AWS (aquí irán comandos aws cli o ansible)"'
      }
    }
  }
}
