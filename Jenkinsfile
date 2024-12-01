pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('video-router:latest')
                }
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                withKubeConfig([credentialsId: 'kubeconfig-id']) {
                    sh 'kubectl apply -f k8s/'
                }
            }
        }
    }
}
