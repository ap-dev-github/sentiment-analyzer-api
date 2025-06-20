
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
    stage('Setup & Lint in Docker') {
      steps {
        script {
          docker.image('cimg/python:3.12-node').inside {
            sh '''
              python -m venv venv
              ./venv/bin/pip install --upgrade pip
              ./venv/bin/pip install -r requirements.txt

              # Linting & Security (ignoring venv, tests)
              ./venv/bin/flake8 . --exclude=venv,tests,.serverless || true
              ./venv/bin/bandit -r . -x venv,tests,.serverless || true
              ./venv/bin/isort . --skip venv --skip tests --skip .serverless --check-only || true
              ./venv/bin/mypy . --exclude '(venv|tests|\\.serverless)' || true
            '''
          }
        }
      }
    }

    stage('Deploy to Lambda') {
      steps {
        script {
          docker.image('cimg/python:3.12-node').inside {
            sh '''
              npm install -g serverless
              ./venv/bin/pip install serverless  # optional
              serverless deploy --stage dev
            '''
          }
        }
      }
    }
  }
}

