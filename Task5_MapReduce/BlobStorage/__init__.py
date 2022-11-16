# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os

from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError


def main(name: str) -> list:
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mapreducetask5;AccountKey=4CsJIxITlvRttjslZXXJApv6+uFLDSK3uVtlqE49hdynm9qr6VkC+EwuqD82wY57PVwXHIkUB3N3+AStNusT6A==;EndpointSuffix=core.windows.net")

    container_name = "blobs"


    containers = blob_service_client.get_container_client(container_name)

    sentence = ""
    blobs = containers.list_blobs()
    for blob in blobs:
        sentence += containers.download_blob(blob.name).readall().decode().replace('\r','')+'\n'

    result = sentence.split('\n')

    return result
