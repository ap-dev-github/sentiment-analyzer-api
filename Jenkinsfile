pipeline {
  agent any

  environment {
    VENV = 'venv'
  }

  stages {
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
          flake8 . --exclude=venv
          bandit -r . || true
          isort . --check-only || true
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
