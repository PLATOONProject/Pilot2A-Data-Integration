# Download base image (Virtuoso so that we can load data to remote endpoint)
FROM kemele/virtuoso:6-stable

USER root
WORKDIR /data

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt-get install -y --no-install-recommends software-properties-common gcc libpq-dev postgresql nano git python3.7 python3-pip

RUN pip3 install psycopg2
RUN pip3 install Flask==1.1.4

# Install SDM-RDFizer
RUN pip3 install rdfizer


CMD ["tail", "-f", "/dev/null"]