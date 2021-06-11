# Download base image ubuntu 20.04
FROM ubuntu:20.04

WORKDIR /data

# Install python3 and python3-pip
RUN apt update && apt install -y gcc python3 python3-pip libpq-dev nano git 

RUN pip3 install psycopg2

# Install SDM-RDFizer
RUN python3 -m pip install rdfizer


CMD ["tail", "-f", "/dev/null"]