pipeline {
  agent any

  environment {
    VENV = 'venv'
    VENV_PYTHON = './venv/bin/python'
    VENV_PIP = './venv/bin/pip'
    VENV_FLAKE8 = './venv/bin/flake8'
    VENV_BANDIT = './venv/bin/bandit'
    VENV_ISORT = './venv/bin/isort'
    VENV_MYPY = './venv/bin/mypy'
    VENV_PYTEST = './venv/bin/pytest'
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

    stage('Lint & Security') {
      steps {
        sh '''
          ${VENV_FLAKE8} . --exclude=venv,tests,.serverless
          ${VENV_BANDIT} -r . -x venv,tests,.serverless || true
          ${VENV_ISORT} . --skip venv --skip tests --skip .serverless --check-only || true
          ${VENV_MYPY} . --exclude '(venv|tests|\\.serverless)' || true
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          ${VENV_PYTEST} tests/ --junitxml=results.xml
        '''
      }
    }

    stage('Deploy to Lambda') {
      steps {
        sh '''
          npm install -g serverless
          ./venv/bin/serverless deploy --stage dev
        '''
      }
    }
  }

  post {
    always {
      junit 'results.xml'
    }
  }
}
