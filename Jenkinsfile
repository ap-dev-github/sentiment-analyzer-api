pipeline {
    agent any

    environment {
        SERVERLESS_ACCESS_KEY = credentials('serverless-access-key') // Jenkins Secret
        PATH = "/usr/bin:$PATH" // Ensure global serverless is accessible
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                sh '''
                    echo "Checking Python version..."
                    python3 --version

                    echo "Checking Node version..."
                    node -v

                    echo "Checking npm version..."
                    npm -v

                    echo "Checking Serverless version..."
                    command -v serverless || { echo "❌ Serverless CLI not found"; exit 1; }

                    echo "✅ Environment looks good."
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing Python virtual environment..."
                    python3 -m venv venv
                    . venv/bin/activate

                    echo "Installing Python dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt

                    echo "Installing Node dependencies..."
                    npm install

                    echo "Installing Serverless WSGI plugin if needed..."
                    npm install --save serverless-wsgi
                '''
            }
        }

        stage('Deploy to AWS Lambda') {
            steps {
                withCredentials([string(credentialsId: 'serverless-access-key', variable: 'SERVERLESS_ACCESS_KEY')]) {
                    sh '''
                        echo "Deploying with Serverless CLI..."
                        serverless deploy --stage dev --verbose
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}
