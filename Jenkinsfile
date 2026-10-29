pipeline {
    agent any 

    environment {
        // Update this to your actual Docker Hub username
        DOCKER_USER = 'YOUR_DOCKERHUB_USERNAME'
        IMAGE_NAME  = 'shopping-bill-app'
    }

    stages {
        // STAGE 1: Source Code
        stage('1. Source Code Check') {
            steps {
                echo "=== STAGE 1: Checking Workspace Files ==="
                // Using 'dir' instead of 'ls' for Windows compatibility
                bat 'dir' 
            }
        }

        // STAGE 2: Continuous Integration (CI)
        stage('2. Automated Testing') {
            steps {
                echo "=== STAGE 2: Running PyTest Suite ==="
                bat 'pytest test_app.py'
            }
        }

        // STAGE 3 & 4: Build & Push Image
        stage('3. Docker Build and Push') {
            steps {
                echo "=== STAGE 3 & 4: Compiling Container & Shipping to Registry ==="
                // Secure username and password injection via Jenkins credentials configuration mapping
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat "docker login -u %USER% -p %PASS%"
                    bat "docker build -t %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER% ."
                    bat "docker push %DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%"
                }
            }
        }

        // STAGE 5: Kubernetes Deployment
        stage('4. Deploy to Kubernetes') {
            steps {
                echo "=== STAGE 5: Updating Cluster Deployment to Tag v${BUILD_NUMBER} ==="
                // Using standard Windows Batch execution to route variables cleanly
                bat """
                    set IMAGE_TAG=%BUILD_NUMBER%
                    kubectl apply --validate=false -f k8s-deployment.yaml
                    kubectl set image deployment/shopping-bill-deployment shopping-bill-container=%DOCKER_USER%/%IMAGE_NAME%:%BUILD_NUMBER%
                """
            }
        }

        // VISUAL PROOF FOR FACULTY GRADING
        stage('5. Cluster Verification') {
            steps {
                echo "=== VERIFICATION: Displaying Live Active Cluster Objects ==="
                bat 'kubectl get deployments'
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }
}
