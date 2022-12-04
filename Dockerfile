#Specifying the base image
FROM python:3.8
#here the dockerfile is pulling the python 3.10 from docker hub which already has python installed so we have all the things we need to have python in our container.

WORKDIR G:\Mi unidad\UOC\Marc\docker-proj\broker

COPY broker.py .
#Here we added the python file that we want to run in docker and define its location.

RUN pip install hbmqtt 
RUN pip install "websockets==8.1"
RUN pip install docker
#Here we installed the dependencies, we are using the pygame library in our main.py file so we have to use the pip command for installing the library

EXPOSE 1883:1883

CMD [ "python3", "broker.py" ]
#lastly we specified the entry command this line is simply running python ./main.py in our container terminal