FROM python:3

RUN apt-get update

RUN apt-get install default-jdk wget -y

RUN apt-get install python3 -y

RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-2.10.1/hadoop-2.10.1.tar.gz

RUN tar -xzvf hadoop-2.10.1.tar.gz

ENV JAVA_HOME /usr/lib/jvm/java-1.11.0-openjdk-amd64

RUN mv hadoop-2.10.1 /usr/local/hadoop

ENV PATH /usr/local/hadoop/bin:$PATH

RUN rm -rf hadoop-2*

RUN pip install pandas

RUN pip install numpy