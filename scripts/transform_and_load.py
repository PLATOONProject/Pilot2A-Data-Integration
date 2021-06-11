#!/usr/bin/env python3

import os  
import sys
import logging
import traceback

from rdfizer.semantify import semantify
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

def transform(configfile, script="/data/scripts/virtuoso-script.sh")
	try:
	    logger.info("Transforming data using " + str(configfile) + " configuration...")
	    outputfolder, status1 = semantify(configfile)
	    if status1:
	        virtuosoIP = os.environ["SPARQL_ENDPOINT_IP"]
			virtuosoUser = os.environ["SPARQL_ENDPOINT_USER"]
			virtuosoPass = os.environ["SPARQL_ENDPOINT_PASSWD"]
			virtuosoPort = os.environ["SPARQL_ENDPOINT_PORT"]
			virtuosoGraph = os.environ["SPARQL_ENDPOINT_GRAPH"]
			outputfolder = os.environ["RDF_DUMP_FOLDER_PATH"]
			try:
	        	os.system( str(script) + " " + virtuosoIP + " " + virtuosoUser + " " + virtuosoPass + " " + virtuosoPort + " " + virtuosoGraph + " " + outputfolder)
	        	logger.info("Semantification sucessful!")
	        except Exception as ex:
	        	logger.error("ERROR while loading data to viruoso! " + str(ex))
	        	exc_type, exc_value, exc_traceback = sys.exc_info()
			    emsg = repr(traceback.format_exception(exc_type, exc_value,
			                                           exc_traceback))
			    logger.error("Exception while semantifying ... " + str(emsg))

	    else:
	        logger.error("Error during semantification of data. Please check your configureation file.")
	    
	except Exception as e:
	    exc_type, exc_value, exc_traceback = sys.exc_info()
	    emsg = repr(traceback.format_exception(exc_type, exc_value,
	                                           exc_traceback))
	    logger.error("Exception while semantifying ... " + str(emsg))
	    