pipeline {
  agent any

  environment {
    VENV = 'venv'
  }

  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/ap-dev-github/sentiment-analyzer-api.git'
      }
    }

    stage('Set Up Python') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Lint & Security') {
      steps {
        sh '''
          . venv/bin/activate
          flake8 .
          bandit -r . || true
          isort . --check-only
          mypy . || true
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest tests/ --junitxml=results.xml
        '''
      }
    }

    stage('Deploy to Lambda') {
      steps {
        sh '''
          . venv/bin/activate
          npm install -g serverless
          serverless deploy --stage dev
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
