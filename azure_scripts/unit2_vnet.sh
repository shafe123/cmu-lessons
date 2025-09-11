RESOURCE_GROUP_NAME=myNetworkingResourceGroup

az group create \
    --name $RESOURCE_GROUP_NAME \
    --location eastus

VNET_NAME=myFirstVNet

az network vnet create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $VNET_NAME

NSG_NAME=myNSG
    
az network nsg create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $NSG_NAME

SUBNET_NAME=myFirstSubnet

az network vnet subnet create \
    --vnet-name $VNET_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $SUBNET_NAME \
    --address-prefix 10.0.0.0/24 \
    --network-security-group $NSG_NAME

VM_NAME=myVM
VM_ADMIN_USERNAME=clouduser

az vm create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $VM_NAME \
    --image UbuntuLTS \
    --storage-sku Standard_LRS \
    --vnet-name $VNET_NAME \
    --subnet $SUBNET_NAME \
    --nsg  "" \
    --admin-username $VM_ADMIN_USERNAME \
    --authentication-type password

az network nsg rule create \
    --resource-group $RESOURCE_GROUP_NAME \
    --nsg-name $NSG_NAME \
    --name Allow-SSH-All \
    --access Allow \
    --protocol Tcp \
    --direction Inbound \
    --priority  100 \
    --source-address-prefixes '*' \
    --source-port-range  '*' \
    --destination-address-prefixes '*' \
    --destination-port-range 22