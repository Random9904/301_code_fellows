Import-Module ActiveDirectory

# User information
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$office = "Springfield, OR"
$title = "TPS Reporting Lead"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$username = $email -replace "@", "_"

# Specify the distinguished name (DN) of the organizational unit (OU) where the user will be created
$ou = "OU=Users,DC=corp.globexpower.com,DC=com" 

# Create a secure password for the user
$password = ConvertTo-SecureString -AsPlainText "Asd(23!z$" -Force

# Use the -WhatIf simulates the action
New-ADUser -SamAccountName $username -UserPrincipalName $email -GivenName $firstName -Surname $lastName -DisplayName $displayName -Title $title -Department $department -EmailAddress $email -Office $office -Enabled $true -AccountPassword $password -ChangePasswordAtLogon $true -Path $ou -WhatIf

# Print to screen what should have happened
Write-Host "User $displayName would have been added to Active Directory if not for -WhatIf."
