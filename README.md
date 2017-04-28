# AzureTag
Automatically tags VM's in Azure from a csv file

The first column is used for ONLY the name of the VM that you wish to tag.\n
Every other column is for the key-value pair.\n
THe first row should be the key that you wish to associate with the tag.\n
Any subsequent row will be the value associated with the key on the first row.\n
This program can only tag VM's that the Azure Account has access too. \n
When you log in, make sure your user account has suffifcient privileges.\n

## AutoTag.ps1 is for tagging VM's ONLY <h2>
## AzureResourceTag.ps1 is for tagging resources that AREN'T VM's <h2>
