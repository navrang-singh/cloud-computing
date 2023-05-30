#### for part 1 ..

step 1 :- install docker on host machine .
                and run all the docker command guven in pdf file .

step 2 :- pull the docker image 
            docker pull python:3.8-slim

step 3 :- mount the python file directory to docker and run a container via ----
            sudo docker run -dit --name=py_container -v ~/(path to python_code.py file):/code  python:3.8-slim

step 4 :- then run --
            sudo docker exec -it py_container /bin/bash
            pip install nltk
            cd code
            python -u python_code.py

step 5 :- thus , part 1 is completed ..





#### for part 2 ...

step 1 :- created file called Dockerfile and docker-compose.yml ( already present in folder so need not to create)

step 2 :- launch EC2 instance and install docker , docker-compose
            a) :- launch an ec2 instance and connect it via ssh . configure the aws credential to fetch the              
                    portfolio_website(given in zip formate) folder from s3 bucket to a folder called 'code' in ec2 instance .
            b) :- install docker via --
                    sudo yum install docker
            c) :- install docker-compose via-
                    sudo yum install python3-pip
                    sudo pip install docker-compose 
            d) :- sudo usermod -a -G docker ec2-user
            e) :- sudo systemctl enable docker.service
            f) :- sudo systemctl start docker.service


step 3 :- navigate to folder where we have docker-compose.yml  file(i.e. = /code/portfolio_website) .

step 4 :-  copy dns address of ec2 instance to a field called ALLOWED HOST in a file called settings.py ( /code/portfolio_website/portfolio_website/settings.py).

step 5 :- then simply run 
            sudo docker-compose up --build

           hurrah ! check the public dns address of ec2 instance our website would be up .....

