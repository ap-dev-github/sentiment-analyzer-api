pipeline {
  agent any

  environment {
    VENV = 'venv'
    PYTHON = './venv/bin/python'
    PIP = './venv/bin/pip'
    FLAKE8 = './venv/bin/flake8'
    BANDIT = './venv/bin/bandit'
    ISORT = './venv/bin/isort'
    MYPY = './venv/bin/mypy'
  }

  stages {
    stage('Set Up Python') {
      steps {
        sh '''
          python3 -m venv venv
          ${PIP} install --upgrade pip
          ${PIP} install -r requirements.txt
        '''
      }
    }

    stage('Lint & Security (ignore venv/tests)') {
      steps {
        sh '''
          ${FLAKE8} . --exclude=venv,tests,.serverless || true
          ${BANDIT} -r . -x venv,tests,.serverless || true
          ${ISORT} . --skip venv --skip tests --skip .serverless --check-only || true
          ${MYPY} . --exclude '(venv|tests|\\.serverless)' || true
        '''
      }
    }

    stage('Deploy to Lambda') {
      steps {
        sh '''
          # Check if npm is available
          if ! command -v npm &> /dev/null; then
            echo "Installing Node.js and npm..."
            curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
            sudo apt-get install -y nodejs
          fi

          npm install -g serverless

          # If you need Python plugin support in serverless
          ${PIP} install serverless

          serverless deploy --stage dev
        '''
      }
    }
  }
}

