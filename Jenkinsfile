pipeline {
  agent any

  environment {
    STAGE = "dev"
  }

  stages {
    stage('Checkout Code') {
      steps {
        checkout scm
      }
    }

    stage('Check Environment') {
      steps {
        sh '''
          echo Checking Python version...
          python3 --version

          echo Checking Node version...
          node -v

          echo Checking npm version...
          npm -v

          echo Checking Serverless version...
          command -v serverless
          echo ✅ Environment looks good.
        '''
      }
    }

    stage('Install Dependencies') {
      steps {
        sh '''
          echo Installing Python virtual environment...
          python3 -m venv venv
          . venv/bin/activate
          echo Installing Python dependencies...
          pip install --upgrade pip
          pip install -r requirements.txt

          echo Installing Node dependencies...
          npm install

          echo Installing Serverless WSGI plugin if needed...
          npm install --save serverless-wsgi
        '''
      }
    }

    stage('Deploy to AWS Lambda') {
      steps {
        withCredentials([
          string(credentialsId: 'serverless-key', variable: 'SERVERLESS_ACCESS_KEY'),
          usernamePassword(credentialsId: 'aws-credentials', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')
        ]) {
          sh '''
            echo Deploying with Serverless CLI...
            serverless deploy --stage $STAGE --verbose
          '''
        }
      }
    }
  }

  post {
    failure {
      echo "❌ Pipeline failed. Check logs above."
    }
    success {
      echo "✅ Deployed successfully to AWS Lambda!"
    }
  }
}

