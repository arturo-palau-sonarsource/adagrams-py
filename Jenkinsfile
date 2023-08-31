node {
  stage('SCM') {
    checkout scm
  }
  stage('Which Java?') {
        sh 'java --version'
        }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
