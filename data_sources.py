import json
import os
from elasticsearch import Elasticsearch
from constants import *


def preprocess_data_sources(directory_path):
    """ Load documents and create a common time fields across different type. """

    documents = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".jsonId"):
            f = open(directory_path + "/" + filename)
            document_json = json.loads(f.read())
            time_field = mappings[document_json['type']]
            if time_field is not None:
                # add common time field
                document_json[common_time_field] = document_json[time_field]
            documents.append(document_json)

    return documents


if __name__ == "__main__":

    # elastic search in a docker container can be used, or a deployment on cloud
    es = Elasticsearch()  # (cloud_id=cluster_id, http_auth=("elastic", cluster_pwd))

    if es.ping():
        print("Connection with Elasticsearch was established.")
    else:
        print("Unable to establish connection with Elasticsearch.")
        exit(1)

    documents = preprocess_data_sources(directory)

    # Ingest data sources into elasticsearch
    for document in documents:
        es.index(index=index_name, ignore=400, doc_type='docket', body=document)
