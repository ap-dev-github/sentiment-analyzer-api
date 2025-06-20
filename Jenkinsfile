pipeline {
  agent any

  environment {
    VENV = 'venv'
    PYTHON = './venv/bin/python'
    PIP = './venv/bin/pip'
  }

  stages {
    stage('Check Environment') {
      steps {
        sh '''
          echo "Checking Python version..."
          python3 --version || { echo "Python not found"; exit 1; }

          echo "Checking Node version..."
          node -v || { echo "Node.js not found"; exit 1; }

          echo "Checking npm..."
          npm -v || { echo "npm not found"; exit 1; }

          echo "Checking Serverless CLI..."
          serverless -v || { echo "Serverless not found"; exit 1; }
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
          serverless deploy --stage dev
        '''
      }
    }
  }

  post {
    failure {
      echo "Pipeline failed. Check logs above 👆"
    }
    success {
      echo "✅ Deployed to AWS Lambda successfully!"
    }
  }
}
