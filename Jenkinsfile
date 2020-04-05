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
            source venv/bin/activate
            pwd
            ls
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
                echo ${MANAGER_IP}
                echo ${DB_ROOT_PASS}
                echo ${SECRET_KEY}
                sshpass ssh -o "StrictHostKeyChecking=no" mo@${MANAGER_IP} <<EOF
                export DB_ROOT_PASS=${DB_ROOT_PASS}
                pwd
                repo="./lottery"
                if [ -d $repo ]
                then
                    rm -rf $repo
                fi
                git clone https://github.com/Ezzmo/Lottery
                cd ~/lottery
                sudo docker stack deploy --compose-file docker-compose.yaml stack
EOF
             '''   
            }
        }
    }
}     