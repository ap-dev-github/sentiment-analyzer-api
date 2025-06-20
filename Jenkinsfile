pipeline {
  agent any

  environment {
    SERVERLESS_ACCESS_KEY = credentials('SERVERLESS_ACCESS_KEY') 
    AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
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
          /usr/bin/serverless --version || {
            echo "❌ Serverless CLI not found"
            exit 1
          }
        '''
      }
    }

    stage('Setup Python Virtualenv') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Deploy to AWS Lambda') {
      steps {
        echo '🚀 Deploying with Serverless CLI...'
        sh '''
          export SERVERLESS_ACCESS_KEY=$SERVERLESS_ACCESS_KEY
          /usr/bin/serverless deploy --stage dev
        '''
      }
    }
  }

  post {
    failure {
      echo "❌ Pipeline failed. Check logs above."
    }
    success {
      echo "✅ Deployment successful!"
    }
  }
}
