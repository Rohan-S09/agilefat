pipeline {
    agent any 

    environment {
        
        DOCKER_USER = 'YOUR_DOCKERHUB_USERNAME'
        IMAGE_NAME  = 'shopping-bill-app'
    }

    stages {
        // STAGE 1: Source Code
        stage('1. Source Code Check') {
            steps {
                echo "=== STAGE 1: Checking Workspace Files ==="

                bat 'dir' 
            }
        }

       
        stage('2. Automated Testing') {
            steps {
                echo "=== STAGE 2: Running PyTest Suite ==="
                bat 'pytest test_app.py'
            }
        }

    }
}
