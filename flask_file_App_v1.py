from flask import Flask, request
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

app = Flask(__name__)

# Set the connection string and container name
connection_string = 'DefaultEndpointsProtocol=https;AccountName=arvindazfundamentals;AccountKey=ZYE0KcG80aloFDauCmWyQMl/2GDlDhuGU4haIaFJHXEm0FYVHK8o7QEJ9IKSp9bF9tAnYO42BD2t+AStt28h3Q==;EndpointSuffix=core.windows.net'
container_name = 'az-fundamentals-container'

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/list-files')
def list_files():
    folder_name = request.args.get('folder_name')
    if folder_name is None:
        return 'Please provide a folder name.'

    # Create the ContainerClient object for the specified container
    container_client = blob_service_client.get_container_client(container_name)

    # List the blobs in the container
    blobs = container_client.list_blobs(name_starts_with=folder_name)

    # Extract the filenames from the blobs
    filenames = [blob.name for blob in blobs]

    # Return the list of filenames
    return '\n'.join(filenames)

if __name__ == '__main__':
    app.run()
