pipeline {
    agent any
    stages{
      stage('Test'){
        steps{
            sh '''
            #!/bin/bash
            sudo apt-get update -y
            sudo apt-get install python3 python3-pip python3-venv -y
            python3 -m venv venv
            . venv/bin/activate
            cd numbers1
            pip3 install -r requirements.txt
            pytest
            cd ../letters1
            pytest
            '''
        }
      }
      stage('ssh into manager'){
        steps{
          sh '''
                ssh mo@${MANAGER_IP} <<EOF
                pwd
                ls -la
            '''
            }
       }

      stage('Deploy'){
        steps{
          sh '''
                export DB_ROOT_PASS=${DB_ROOT_PASS}
                export VERSION=${VERSION}
                rm -rf lottery
                git clone https://github.com/Ezzmo/lottery
                cd ./lottery
                docker stack deploy --compose-file docker-compose.yaml lottery
             '''   
            }
        }
    }
}     