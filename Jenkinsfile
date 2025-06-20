pipeline {
  agent any

  environment {
    VENV = 'venv'
    PYTHON = './venv/bin/python'
    PIP = './venv/bin/pip'
  }

  stages {
    stage('Install Python Deps') {
      steps {
        sh '''
          python3 -m venv venv
          ${PIP} install --upgrade pip
          ${PIP} install -r requirements.txt
        '''
      }
    }

    stage('Lint & Security') {
      steps {
        sh '''
          ./venv/bin/flake8 . --exclude=venv,tests,.serverless || true
          ./venv/bin/bandit -r . -x venv,tests,.serverless || true
          ./venv/bin/isort . --skip venv --skip tests --skip .serverless --check-only || true
          ./venv/bin/mypy . --exclude '(venv|tests|\\.serverless)' || true
        '''
      }
    }

    stage('Deploy to AWS Lambda') {
      steps {
        sh '''
          npm install -g serverless
          ./venv/bin/pip install serverless
          serverless deploy --stage dev
        '''
      }
    }
  }
}
