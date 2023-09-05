node {
  env.JAVA_HOME="${tool 'Java_17'}"
  env.PATH="${env.JAVA_HOME}/bin:${env.PATH}"
  sh 'java -version'
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
