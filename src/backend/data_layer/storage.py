from azure.storage.blob import BlobServiceClient, StandardBlobTier
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

conn_str = os.getenv("BLOB_CS")
container_name = "code-tales"

blob_service_client = BlobServiceClient.from_connection_string(conn_str)

def upload_blob(local_path, blob_name):
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)

    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)

    print("Data located in: " + local_path)
    with open(local_path, "rb") as data:
        blob_client.upload_blob(data, standard_blob_tier=StandardBlobTier.COLD)

