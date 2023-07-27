node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool name: 'SonarScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
