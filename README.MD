Thi code can be used to generate temporary credentials (with MFA).



#### Usage

Make sure that you add the path to the directory to the PYTHONPATH environment variable

>from aws_creds import aws_creds

>aws_access_key_id, aws_secret_access_key, _ = **aws_creds.get_credentials()**  
##to get permanent credentials

>aws_access_key_id, aws_secret_access_key, aws_session_token = **aws_creds.get_credentials("Temp")**  
##to get temporary credentials

>**aws_creds.update_temp_credentials("123456")**  
##to update the temporary credentials

>**aws_creds.get_credentials_expiry_info()**  
#to print info about token expiry 


#### Dependencies
The code expects two files - "credentials"  and "config.yaml" - inside the BASEDIR.

"Permanent credentials" are expected within the credentials file.

MFA_ARN needs to have your mfa ARN name

"update_temp_credentials" requires a valid 6-digit MFA code 
