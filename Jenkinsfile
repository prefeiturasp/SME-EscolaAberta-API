pipeline {
    agent {
      node { 
        label 'py36-terceirizadas'
	    }
    }
    
    options {
      buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
      disableConcurrentBuilds()
      skipDefaultCheckout()  
    }
           
    stages {
        stage('CheckOut') {
        steps {
          checkout scm	
        }
       }

       stage('Testes') {
        steps {
          sh 'pip install --user --upgrade pip'    
          sh 'pip install -r requirements.txt --user'
          sh 'pip install --user tox && tox -e test'
        }
        
       }

       stage('Analise codigo') {
	     when {
           branch 'dev'
         }
        steps {
          sh 'sonar-scanner \
              -Dsonar.projectKey=SME-EscolaAberta-API \
              -Dsonar.sources=. \
              -Dsonar.host.url=http://sonar.sme.prefeitura.sp.gov.br \
              -Dsonar.login=419686492d717d258ec6cdd3111c5e0bc0c47236'
        }
       }
      
       stage('Build docker DEV') {
         when {
           branch 'dev'
         }
        steps {
          sh 'echo build docker image desenvolvimento'
          // Start JOB para build das imagens Docker e push SME Registry
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "3db40387-ad07-41f6-b83f-064872e2ada5",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
           }
        }
       }        
       
       stage('Deploy DEV') {
         when {
           branch 'dev'
         }
        steps {
       
       
           //Start JOB de deploy Kubernetes 
          sh 'echo Deploy ambiente desenvolvimento'
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "6feb52aa-b3ca-4b14-8a05-64206087ad72",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
          }
        } 
       }
       
       stage('Build docker HOM') {
         when {
           branch 'homolog'
         }
        steps {
          
         sh 'echo Deploying ambiente homologacao'
                
          // Start JOB para build das imagens Docker e push SME Registry
      
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
                             
              //JOB DE BUILD
              jobId: "b3525d3b-3eb5-42a1-8d80-74b201b3adf9",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
          }
        }
       } 
          
        stage('Deploy HOM') {
         when {
           branch 'homolog'
         }
        steps {  
          timeout(time: 24, unit: "HOURS") {
          // telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Requer uma aprovação para deploy !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n")
            input message: 'Deseja realizar o deploy?', ok: 'SIM', submitter: 'marcos_nastri, calvin_rossinhole, ollyver_ottoboni, kelwy_oliveira, pedro_walter'
          } 
         
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "3210db50-a7a3-41bf-8cd3-e3b0130b9ade",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
          }
        }
       }

       stage('Build docker PROD') {
         when {
           branch 'master'
         }
        steps {
          
            sh 'echo Build image docker Produção'
          // Start JOB para build das imagens Docker e push SME Registry
      
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
                             
              //JOB DE BUILD
              jobId: "038e590f-cfba-40dd-92b2-be83b425c17e",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
               //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
          }
        }
       } 
          
        stage('Deploy PROD') {
         when {
           branch 'master'
         }
        steps {
          timeout(time: 24, unit: "HOURS") {
          // telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Requer uma aprovação para deploy !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n")
            input message: 'Deseja realizar o deploy?', ok: 'SIM', submitter: 'marcos_nastri, calvin_rossinhole, ollyver_ottoboni, kelwy_oliveira, pedro_walter'
          }
        
          script {
            step([$class: "RundeckNotifier",
              includeRundeckLogs: true,
              jobId: "661ac21b-a60e-47eb-b24a-cc4761ec3147",
              nodeFilters: "",
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: "Rundeck-SME",
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: "",
              tailLog: true])
          }
        }
       }
    } 
  	   
  post {
    always {
      echo 'One way or another, I have finished'
    }
    success {
      telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Esta ok !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n\n Uma nova versão da aplicação esta disponivel!!!")
    }
    unstable {
      telegramSend("O Build ${BUILD_DISPLAY_NAME} <${env.BUILD_URL}> - Esta instavel ...\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
    }
    failure {
      telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME}  - Quebrou. \nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
    }
    changed {
      echo 'Things were different before...'
    }
    aborted {
      telegramSend("O Build ${BUILD_DISPLAY_NAME} - Foi abortado.\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
    }
  }
}
