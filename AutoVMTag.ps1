#User:firstname.lastname
#PM:(Blank)
#Project:(Resource Group Name)
#AutoOn:False
#AutoOff:True
#Group:crc-itim/vpap-na/vpap-pe/vpap-rt/vpwt-nt/vpwt-pa
#Backup:False
#Usage-type:application/core/external/workload

#Log into Azure
Login-AzureRmAccount
#Get list of all the VM's
$list = get-azurermvm |sort-object name

#Read the Keys and values from csv
$reader = [System.IO.File]::OpenText("tag.csv")
$tags.clear()
$reader.readLine()

while($null -ne ($line = $reader.ReadLine())) {
    $values = $line.Split(',')
    foreach ($element in $list){
        if($values[0] -eq $element.name){
            $values[3]=$element.ResourceGroupName
            $tags += @{User=$values[1];PM='';Project=$values[3];AutoOn=$values[4];AutoOff=$values[5];Backup=$values[7];'Usage-Type'=$values[8]}
            if($values[6]){
               $tags+=@{Group=$values[6]}
            }
            #Set-AzureRmResource -ResourceGroupName $values[3] -ResourceType "Microsoft.Compute/VirtualMachines" -name $values[0] -Tag $tags -Force
            $tags
            break
        }
    }

    echo '------------------------'
    #$tags
    $tags.clear()

}

#Set-AzureRmRe source -ResourceGroupName "crc-msdn-research-coopstudents1" -ResourceType "Microsoft.Compute\virtualmachines" -name "crcbriannorman1" -Tag @{test="test"}
