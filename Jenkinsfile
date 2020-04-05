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
      stage('Deploy'){
        steps{
          sh '''
                ssh mo@${MANAGER_IP} <<EOF
                export DB_ROOT_PASS=${DB_ROOT_PASS}
                rm -rf Lottery
                git clone https://github.com/Ezzmo/Lottery
                cd ./Lottery
                docker stack deploy --compose-file docker-compose.yaml Lottery
EOF
             '''   
            }
        }
    }
}     