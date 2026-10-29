pipeline {
    agent any 

    environment {
    
        DOCKER_USER = 'YOUR_DOCKERHUB_USERNAME'
        IMAGE_NAME  = 'shopping-bill-app'
    }

    stages {
     
        stage('1. Source Code Check') {
            steps {
                echo "=== STAGE 1: Checking Workspace Files ==="
                sh 'ls' 
            }
        }

        stage('2. Automated Testing') {
            steps {
                echo "=== STAGE 2: Running PyTest Suite ==="
                sh 'pytest test_app.py'
            }
        }

     
        stage('3. Docker Build and Push') {
            steps {
                echo "=== STAGE 3 & 4: Compiling Container & Shipping to Registry ==="
                
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "docker login -u ${USER} -p ${PASS}"
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ."
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo "=== STAGE 5: Updating Cluster Deployment to Tag v${BUILD_NUMBER} ==="
                sh '''
                    export IMAGE_TAG=${BUILD_NUMBER}
                    envsubst < k8s-deployment.yaml | kubectl apply --validate=false -f -
                '''
            }
        }

        stage('5. Cluster Verification') {
            steps {
                echo "=== VERIFICATION: Displaying Live Active Cluster Objects ==="
                sh 'kubectl get deployments'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
