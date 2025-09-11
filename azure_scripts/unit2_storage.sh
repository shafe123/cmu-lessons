# create storage account
STORAGE_ACCOUNT_NAME=<unique_name>

az storage account create \
    --name $STORAGE_ACCOUNT_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --location eastus \
    --sku Standard_LRS \
    --kind StorageV2

# create storage container
CONTAINER_NAME=myblobcontainer

az storage container create \
    --name $CONTAINER_NAME \
    --account-name $STORAGE_ACCOUNT_NAME

# upload a blob
FILE_TO_UPLOAD=hello.txt
echo "Hello Azure Storage" > $FILE_TO_UPLOAD

BLOB_NAME=uploaded_hello.txt

az storage blob upload \
    --file $FILE_TO_UPLOAD \
    --container-name $CONTAINER_NAME \
    --name $BLOB_NAME \
    --account-name $STORAGE_ACCOUNT_NAME

# download a blob
DOWNLOADED_FILENAME=downloaded_hello.txt

az storage blob download \
    --container-name $CONTAINER_NAME \
    --name $BLOB_NAME \
    --file $DOWNLOADED_FILENAME \
    --account-name $STORAGE_ACCOUNT_NAME