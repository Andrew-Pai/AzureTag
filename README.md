# AzureTag
Automatically tags VM's in Azure from a csv file

The first column is used for ONLY the name of the resource that you wish to tag.

Every other column is for the key-value pair.

THe first row should be the key that you wish to associate with the tag.

Any subsequent row will be the value associated with the key on the first row.

This program can only tag VM's that the Azure Account has access too. 

When you log in, make sure your user account has suffifcient privileges.

Look at **tag.csv** for an example

## AutoTag.ps1 is for tagging VM's ONLY <h2>
## AzureResourceTag.ps1 is for tagging resources that AREN'T VM's <h2>
