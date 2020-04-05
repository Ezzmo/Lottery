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
                ssh -o "StrictHostKeyChecking=no" mo@${MANAGER_IP} <<EOF
                export DB_ROOT_PASS=${DB_ROOT_PASS}
                dir="./lottery"
                if [ -d $dir ]
                then
                    rm -rf $dir
                fi
                git clone https://github.com/Ezzmo/Lottery
                cd ./lottery
                sudo docker stack deploy --compose-file docker-compose.yaml lottery
EOF
             '''   
            }
        }
    }
}     