# Download base image (Virtuoso so that we can load data to remote endpoint)
FROM kemele/virtuoso:6-stable

WORKDIR /data

# Install python3 and python3-pip
RUN apt update && apt install -y gcc python3 python3-pip libpq-dev nano git 

RUN pip3 install psycopg2

# Install SDM-RDFizer
RUN python3 -m pip install rdfizer


CMD ["tail", "-f", "/dev/null"]