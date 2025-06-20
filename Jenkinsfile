pipeline {
  agent any

  environment {
    // Add serverless CLI directory to PATH
    PATH = "/mnt/c/Users/inbox/AppData/Roaming/npm:$PATH"
    VENV = 'venv'
    PYTHON = './venv/bin/python'
    PIP = './venv/bin/pip'
  }

  stages {
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
          /mnt/c/Users/inbox/AppData/Roaming/npm/serverless --version
        '''
      }
    }

    stage('Setup Python Virtualenv') {
      steps {
        sh '''
          python3 -m venv ${VENV}
          ${PIP} install --upgrade pip
          ${PIP} install -r requirements.txt
        '''
      }
    }

    stage('Deploy to AWS Lambda') {
      steps {
        sh '''
          echo "Deploying with Serverless CLI..."
          /mnt/c/Users/inbox/AppData/Roaming/npm/serverless deploy --stage dev
        '''
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
