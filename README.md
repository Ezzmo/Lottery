# Raffle/prize code generator

# Introduction 

This project was to build a simple object generating app split up into containerized microservices and depoloyed as a docker swarm. In addition, the ansible was sued in order to preconfigure the virtual machines used for the deployment.


# Architechture
![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/App%20architechture.png "Logo Title Text 1")



# Risk Assessment
![alt text](https://github.com/Ezzmo/Lottery/blob/master/documentation/Risk%20assessment.PNG "Logo Title Text 1")

pic

# Project Tracking

To track my project, I used a trello kanban board. The aim for each spring was to complete at least one card. By the project deadline, everything was in progress or completed, with the database, documentation and some tests were incomplete. 
![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/Trello%20initial.PNG "Logo Title Text 1")
![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/trello%20midway.PNG "Logo Title Text 1")
![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/trello%20deadline.PNG "Logo Title Text 1")

# MoSCoW Priority

For this project I identified a MoSCoW priority:

MUST:
- Number and letter generating services
- Backend service
- Frontend service
- Deploy app via docker swarm
- Deploy app across multiple VMs
- Test app and use it to drive development

SHOULD:
- Use database to store winners
- Automate environment set up completely
- Use load balancer

Could:
- Build frontend with good aesthetics


# Testing

Automated testing was incomplete, with the frontend being untested. Howver, Postman was used for manual testing of the app routing and responses. Postman was used throughout development, and the number and letter services test scripts were designed beforehand.

# Jenkins
![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/Jenkins.PNG "Logo Title Text 1")

A CI pipeline was implemented through Jenkins, by using a Jenkinsfile to configure the testing and deployment. The Pipeline contained two stages, testing and deploying.

# Docker Swarm

The containerization of the app was handled through the use of Docker, and Docker swarm. Each microservice was built into its own image and pushed to a remote repository (Docker hub). The number of replicas was decided in the docker-compose.yaml file, however, on this occasion only 1 replica was used due to a lack of resource causing stability issues.

# Ansible

Using ansible playbooks, the environments of the VMs were set up. This included:

- Installation of docker on the VMs (swarm-master and swarm-worker are two of those)
- Installation of Jenkins on the Jenkins VM and the addition of a Jenkins user to each VM
- Installation of NGINX on the load balancer VM


# User Stories 

- As a User I would like to be able to generate account numbers
- As a User I would like to be able to access my account.
- As a Developer I would like access to the winners details
- As a product owner I would like for any changes to be rolled out automatically with ease


# CI Pipeline

![alt text](https://github.com/Ezzmo/lottery/blob/master/documentation/pipeline.jpg "Logo Title Text 1")

# Tests

The generating services were tested using pytest, and the routes were tested using Postman.

# Discussion

The end result of this project has an MVP that is acceptable and successfuly demonstrates the feature of a CI pipeline, docntainerization and swarm deployment.

# Future Improvements

More robust testing; all shortcomings are due to inxperience with these new technolgies and thus taking a long time to debug.
Better time management: this would allow more efficient debugging.
