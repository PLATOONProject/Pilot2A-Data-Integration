# Pilot2A-Data-Integration

This repository contains basic settings for Pilot 2A Knowledge Graph. 

- `mappings` - contain RML mappings of available Pilot 2A data sources using the `PLATOON` semantic data model v? .
- `config.ini` - configuration file for materializing the Knowledge Graph using [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer).
- `docker-compose.yml` - docker compose setup for transforming data to RDF and load it to `Virtuoso` triple store.

# Creating RDF Dump using SDM-RDFizer


## Configure (Data Source credentials, output location, etc)

Edit `config.ini` file as follows:

Set the main directory in the `[default]` section 

```bash
	
[default]
main_directory: ./

```
Main directory for this setting is now, current folder. 

```bash

[datasets]
number_of_datasets: 8
output_folder: ${default:main_directory}/rdf-dump
all_in_one_file: yes
remove_duplicate: yes
name: pilot2a-observation-data	
dbtype: mysql
```


In `datasets` section, you can set global parameters such as the number of datasets, output folder, how dump file should be created, name of the dump file (if dump is set to be saved in one file), database type, etc.

-  *`number_of_datasets`* - how many datasets to transforms (create an rdf dump for). e.g., 8
- *`output_folder`* - sets where the transformed dump to be saved, e.g., `${default:main_directory}/rdf-dump` 
- *`all_in_one_file`* - takes `yes` or `no` values, and sets whether to put all datasets in one file or in a separate file names. If set `yes`, then the `name` parameter will be used as the name of the file, i.e., "$(name)".nt and stored in `output_folder`
- *`remove_duplicate`* - takes `yes` or `no` values, and sets wherther duplicates should be removed while generatting RDF triples from single source with different tables/files or multiple data sources that might have duplicate values while applying the transformation.
- *`name`* - sets the name of output RDF dump, if `all_in_one_file` parameter is set to `yes`.
- *`dbtype`* - sets the data source type, e.g., `csv`, `mysql`, `postgres`, `json`, `xml`, etc.

Once the `[default]` and `[datasets]` section is configures, then you need to put as many dataset specific setting as the `number_of_datasets` specified in `[datasets]` section.
For example, the first dataset, `wind_farm_properties`, is configured as follows

```bash

[dataset1]
name: pilot2a_wind_farm_props
user:root
password:1234
host:192.168.0.2
port:3306
db:platoon_db
mapping: ${default:main_directory}/mappings/Wind-Farm/wind-farm.ttl

```

Note on the dataset number, `[dataset1]`, dataset number 1 out of 8 datasets in this configuration. Each dataset will have its own configuration param values. In the snippet above, we set the name of dataset (this name will be used if `all_in_one_file` param of the global param is set to `no`). Other settings include: `user` and `password` - user name and password of the user to access the database, `host`, `port`, and `db` - hostname, port and database name of the dataset (dataset1->wind_farm_props), and finally the `mapping` param specifies where the RML mapping rules file is located. RML mapping rules need to conform the [RML Spec](http://rml.io/specs/rml/).

There need to be at least *8* unique names of `[dataset_n]` sections specifiying the parameters of each datasets in this configuration.

## Run `rdfizer` tool to create the RDF dump according to the above configuration and mapping files included in this config.

### Option 1: Using the `rdfizer` tool directly 

1. Install `SDM-RDFizer`

```bash

python3 -m pip install rdfizer

```

2. Then run `rdfizer` script

```bash

cd Pilot2A-Data-Integration/
python3 -m rdfizer -c config.ini

```

This will create the RDF dumps according the configuration file, `config.ini`.

### Option 2: Using docker

1. Run the docker compose file included in this repository.

(Prerequisite: *Docker-ce*, *Docker-compose*)

```bash

docker-compose up -d

```

2. Then run `rdfizer` script.

The docker container created above using the docker-compose.yaml file will attach this repository as volume at `/data` endpoint. So running `rdfizer` script as follows will yield the same result as `Option 1` above.

```bash

cd Pilot2A-Data-Integration/
docker exec -it sdmrdfizer python3 -m rdfizer -c /data/config.ini 

```

This will create the RDF dumps according the configuration file, `config.ini`, and store the RDF dump in `/data/` volume, which in turn in "Pilot2A-Data-Integration/"

3. Load the RDF dump to Virtuoso


To load the generated RDF dump in step 2, we will use a script included in `/data/scripts/` folder as follows:

```bash

docker exec -it sdmrdfizer /data/scripts/load_to_virtuoso.py 

```

Before running this, make sure you update the environmental variable in the `docker-compose.yml` file as follows:


```bash

environment:
      - SPARQL_ENDPOINT_IP=pilot2akg # Make sure this IP address is same as pilot2akg containers IP (to get the IP just run: docker inspect pilot2akg | grep IPAddress)
      - SPARQL_ENDPOINT_USER=dba
      - SPARQL_ENDPOINT_PASSWD=dba
      - SPARQL_ENDPOINT_PORT=1116
      - SPARQL_ENDPOINT_GRAPH=http://platoon.eu/Pilot2A/KG 
      - RDF_DUMP_FOLDER_PATH=/data/rdf-dump

```