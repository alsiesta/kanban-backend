from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential, DefaultAzureCredential # Needed for Azure Managed Identity
from django.core.files.storage import Storage
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_CONTAINER = os.getenv('AZURE_CONTAINER')
AZURE_ACCOUNT_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/'

def get_azure_credentials():
    return ClientSecretCredential(
        tenant_id=os.getenv('AZURE_TENANT_ID'),
        client_id=os.getenv('AZURE_CLIENT_ID'),
        client_secret=os.getenv('AZURE_CLIENT_SECRET')
    )  # Or use DefaultAzureCredential() for production with Managed Identity
    
class AzureBlobStorage(Storage):
    def __init__(self):
        self.credential = get_azure_credentials()
        self.blob_service_client = BlobServiceClient(account_url=AZURE_ACCOUNT_URL, credential=self.credential)
        
    def get_blob_client(self, name):
        return self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
    
    def _open(self, name, mode='rb'):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        return blob_client.download_blob().readall()

    def _save(self, name, content):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        blob_client.upload_blob(content, overwrite=True)
        return name
    
    def exists(self, name):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        try:
            blob_client.get_blob_properties()
            return True
        except Exception as e:
            return False

    def url(self, name):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        return blob_client.url

    def listdir(self, path):
        container_client = self.blob_service_client.get_container_client(AZURE_CONTAINER)
        blobs = container_client.list_blobs(name_starts_with=path)
        files = []
        dirs = set()
        for blob in blobs:
            blob_name = blob.name
            if '/' in blob_name[len(path):]:
                dir_part = blob_name[len(path):].split('/', 1)[0]
                dirs.add(dir_part)
            else:
                files.append(blob_name[len(path):])
        return list(dirs), files

    def size(self, name):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        properties = blob_client.get_blob_properties()
        return properties.size

    def delete(self, name):
        blob_client = self.blob_service_client.get_blob_client(container=AZURE_CONTAINER, blob=name)
        blob_client.delete_blob()