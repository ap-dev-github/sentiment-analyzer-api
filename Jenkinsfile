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
          ./venv/bin/pip install --upgrade pip
          ./venv/bin/pip install -r requirements.txt
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
          npm install -g serverless
          ./venv/bin/pip install serverless  # Optional: if needed for Python env
          serverless deploy --stage dev
        '''
      }
    }
  }
}

