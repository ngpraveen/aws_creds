This module can be used to access and update temporary credentials (with MFA).



#### Usage

Make sure that you:
 - add the path to the directory to the PYTHONPATH environment variable (for importing)
 - add credentials and config.yaml files
 - update parameters defined in credentials and config.yaml files

>from aws_creds import creds

>aws_access_key_id, aws_secret_access_key, _ = **creds.get_credentials()**  
##to get permanent credentials

>aws_access_key_id, aws_secret_access_key, aws_session_token = **creds.get_credentials("Temp")**  
##to get temporary credentials

>**creds.update_temp_credentials("123456")**  
##to update the temporary credentials

>**creds.get_credentials_expiry_info()**  
#to print info about token expiry 


#### Dependencies
The code expects two files - "credentials"  and "config.yaml" - inside the BASEDIR.

"Permanent credentials" are expected within the credentials file.

MFA_ARN needs to have your mfa ARN name

"update_temp_credentials" requires a valid 6-digit MFA code 
