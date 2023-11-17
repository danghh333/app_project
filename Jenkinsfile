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
            def scannerHome = tool 'SonarQube Scanner 5.14.0.78575'
            withSonarQubeEnv('sonar') {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
  }
}