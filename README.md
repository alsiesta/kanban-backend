## Use Azure Storage for Django media and static files

### Settings in Azure
Create Azure Storage Account and make sure in the storage account, 
1. Under "Networking" **Public network access** the [Enabled from all networks] option *'is checked'*
2. Under "Configuration" **Allow Blob anonymous access** the [Enabled] *'is checked'*
3. On the "container level" select **Change access level** at the related top nav-bar the ***Anonymous access level*** is set to [Blob (anonymous read access for blobs only)] '*is selected*'

### Settings in the Django App

#### Option A - using Storage Account Key in code
Then in the settings.py of the Django Project do the following changes
```
/settings.py

from django.core.files.storage import Storage //CRITICAL IMPORT to address and extend/overwrite Django storage 

INSTALLED_APPS = [
    ...,
    'storages',  # Add this line
]

... end somewhere towards the end

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'your_account_name'
AZURE_ACCOUNT_KEY = 'your_account_key'
AZURE_CONTAINER = 'your_container_name'
AZURE_OVERWRITE_FILES = True  # Set to True or False based on your preference
AZURE_URL_EXPIRATION_SECS = None
AZURE_SSL = True

# In case you want to use Azure for static files as well
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_STATIC_CONTAINER = 'your_static_container_name'

```

#### Option B - using Managed Identity
Use Azure Managed Identity by adding this to settings.py
```
DEFAULT_FILE_STORAGE = 'home.azure_storage.AzureBlobStorage' # this complete class is defined in home/azure_storage.py and it handles all the storage operations used by Django Admin and other parts of the application

AZURE_ACCOUNT_NAME = 'dlastor'
AZURE_CONTAINER = 'dla-web-media'
AZURE_ACCOUNT_URL = 'https://dlastor.blob.core.windows.net/'

```
And create a complete **AzureBlobStorage Class**, that manages the Django storage operations. It resides currently in the **home app** and you need to import there the following dependencies:
```
from django.core.files.storage import Storage //CRITICAL IMPORT to address and overwrite/extends Django storage 

from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential, DefaultAzureCredential
```
*Note:* 
**ClientSecretCredential** is needed, when working in Dev-Mode locally.  
**DefaultAzureCredential** is needed in production to allow Authentication when the App is hosted as Azure resource.

### Important CORS setting
Also in settings.py set the following:
```
//settings.py

CSRF_TRUSTED_ORIGINS = ['https://<your_webapp_name>.azurewebsites.net']
```