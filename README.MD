The following code can be used to generate temporary credentials (with MFA).

#### Usage

>aws_access_key_id, aws_secret_access_key, _ = **get_credentials()**  
##to get permanent credentials

>aws_access_key_id, aws_secret_access_key, aws_session_token = **get_credentials("Temp")**  
##to get temporary credentials

>**update_temp_credentials("123456")**  
##to update the temporary credentials

>**get_credentials_expiry_info()**  
#to print info about token expiry 


#### Dependencies
The code expects a file "credentials" inside the BASEDIR.

"Permanent credentials" are expected within the credentials file.

MFA_ARN needs to be your mfa ARN 

"update_temp_credentials" requires a valid 6-digit MFA code 
