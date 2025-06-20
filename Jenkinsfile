pipeline {
  agent any

  environment {
    VENV_DIR = '.venv'
  }

  stages {
    stage('Check Environment') {
      steps {
        sh '''
          echo Checking Python version...
          python3 --version || { echo "Python 3 not found"; exit 1; }

          echo Checking Node version...
          node -v || { echo "Node.js not found"; exit 1; }

          echo Checking npm version...
          npm -v || { echo "npm not found"; exit 1; }

          echo Checking Serverless version...
          if ! command -v serverless &> /dev/null; then
            echo "Serverless CLI not found"
            exit 1
          fi
        '''
      }
    }

    stage('Setup Python Virtualenv') {
      steps {
        sh '''
          echo Creating virtual environment...
          python3 -m venv $VENV_DIR
          source $VENV_DIR/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Deploy to AWS Lambda') {
      steps {
        withCredentials([string(credentialsId: 'SERVERLESS_ACCESS_KEY', variable: 'SERVERLESS_ACCESS_KEY')]) {
          sh '''
            echo Deploying with Serverless CLI...
            export SERVERLESS_ACCESS_KEY=$SERVERLESS_ACCESS_KEY
            serverless deploy --stage dev
          '''
        }
      }
    }
  }

  post {
    failure {
      echo '❌ Pipeline failed. Check logs above.'
    }
    success {
      echo '✅ Deployment successful!'
    }
  }
}

