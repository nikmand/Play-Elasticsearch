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

    es = Elasticsearch(cloud_id=cluster_id, http_auth=("elastic", cluster_pwd))

    if es.ping():
        print("Connection with Elasticsearch was established.")
    else:
        print("Unable to establish connection with Elasticsearch.")
        exit(1)

    documents = preprocess_data_sources(directory)

    # Send ingest data sources into es
    for document in documents:
        print(document['type'])
        es.index(index=index_name, ignore=400, doc_type='docket', body=document)


    # result = es.search(
    #     index="myindex")
    #
    # print(result)

    # es.indices.refresh(index_name)
    # cnt = es.cat.count(index_name, params={"format": "json"})
    #
    # # es.indices.delete(index=index_name, ignore=[400, 404])
    #
    # search_param = {
    #     "query": {
    #         "match": {
    #             "type": "BuildingOperation"
    #         }
    #     }
    # }
    # #
    # response = es.search(index=index_name, body=search_param)
    # all_documents = response['hits']['hits'] # list of results
    #
    # for document in all_documents:
    #     print(document['_source']['createdAt'])
