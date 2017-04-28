#Log into Azure
Login-AzureRmAccount
#Get list of all the VM's
$list = Get-AzureRmResource |sort-object name
#Reads tags from csv file
$reader = [System.IO.File]::OpenText("C:\Users\CRCIMIT\Desktop\VM\tag.csv")
$tags=@{}
$tags.clear()
$key=@()
$key.clear()
#Separates each line into the resource name, and the tags
$line = ($reader.readLine().split(','))
$line = $line[1..$line.Length]
$counter =0
foreach ($values in $line){
    #Adds the keys to an array
    $key+=$values
}

#Loops through rest of the CSV
while($null -ne ($line = $reader.ReadLine())) {

    $values = $line.Split(',')
    #Loops through each resource from Get-AzureRMResource
    foreach ($element in $list){
        #Check to make sure the Resource is not a virtual Machine
        if($element.ResourceType -ne 'Microsoft.Compute/virtualMachines'){
            if($values[0] -eq $element.name){

                for($i=0;$i -lt $key.Length; $i++){
                    #If the key is Project, it'll put the resource group name for the value instead of what was in the csv
                    if($key[$i] -eq 'Project'){
                        $values[$i+1] = $element.ResourceGroupName
                        $tags+= @{$key[$i]=$values[$i+1]}
                    }elseif($key[$i] -eq 'Group'){
                        #For keys that are 'Group', checks to see if there is an associated value or not
                        #Will tag if there is a value
                        if($values[$i+1]){
                            $tags+=@{Group=$values[$i+1]}
                        }
                    }else{
                        #If key is not 'Project' or 'Group' then it'll add they key-value to a hash-table in $tags
                        $tags+=@{$key[$i]=$values[$i+1]}
                    }
                
                }
                #THis is the command that actually adds the tags to the correct resource
                Set-AzureRmResource -ResourceGroupName $element.ResourceGroupName -ResourceType $element.ResourceType -ResourceName $element.ResourceName -Tag $tags -Force
                $tags
                $counter++
                #Break the loop that is going through each resource, to move on to the next resource name to be tagged
                break
            }

        }
    }

    echo '------------------------'
    $tags.clear()

}
$counter