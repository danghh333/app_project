pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        sh 'echo "Hello World"'
      }
    }
    stage('scan') {
        steps {
            withSonarQubeEnv('sonar') {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
  }
}