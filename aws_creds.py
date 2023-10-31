import boto3
from configparser import ConfigParser
import yaml
import os


# read basedir and mfa arn from config.yaml file
with open(f'{os.path.dirname(__file__)}/config.yaml', 'r') as f:
    _config = yaml.safe_load(f)

BASEDIR = _config['baseDir']
MFA_ARN = _config['mfaArn']



def get_credentials(profile="default", only_expiration=False):
    """Returns a set of credentials. It can be either 
    the "default" profile's credentials or any other profile's credentials"""
    
    
    parser = ConfigParser()
    _ = parser.read(f"{BASEDIR}/credentials")

    aws_access_key_id = parser.get(profile, "aws_access_key_id")
    aws_secret_access_key = parser.get(profile, "aws_secret_access_key")
    
    try:
        aws_session_token = parser.get(profile, "aws_session_token")
    except:
        aws_session_token = None
        
        
    if only_expiration:
        try:
            aws_session_token_expiration = parser.get(profile, "aws_session_token_expiration")
        except:
            aws_session_token_expiration = None
            
        return aws_session_token_expiration
    
    return aws_access_key_id, aws_secret_access_key, aws_session_token


def update_temp_credentials(mfa_code):

    aws_access_key_id, aws_secret_access_key, _ = get_credentials()
    sts_client = boto3.client('sts', 
                          aws_access_key_id = aws_access_key_id,
                         aws_secret_access_key = aws_secret_access_key)
    res = sts_client.get_session_token(SerialNumber=f"{MFA_ARN}", TokenCode=str(mfa_code))
    cred = res["Credentials"]
    
    
    temp_aws_access_key_id = cred["AccessKeyId"]
    temp_aws_secret_access_key = cred["SecretAccessKey"]
    temp_aws_session_token = cred["SessionToken"]
    temp_aws_session_token_expiration = cred["Expiration"].strftime("%Y-%m-%d %H:%M:%S")
    
    parser = ConfigParser()
    _ = parser.read(f"{BASEDIR}/credentials")
    
    if not parser.has_section("Temp"):
        parser.add_section("Temp")
        
    parser.set("Temp", "aws_access_key_id", temp_aws_access_key_id)
    parser.set("Temp", "aws_secret_access_key", temp_aws_secret_access_key)
    parser.set("Temp", "aws_session_token", temp_aws_session_token)
    parser.set("Temp", "aws_session_token_expiration", temp_aws_session_token_expiration)
    
    with open(f"{BASEDIR}/credentials", "w") as f:
        parser.write(f)

                

def get_credentials_expiry_info():
    import datetime
    expiry = get_credentials("Temp", only_expiration=True)
    expiry = datetime.datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.utcnow()
    td = (expiry - now)

    if now >= expiry:
        print("The token has expired. Please call 'update_temp_credentials' to update the token")
    else:
        td = (expiry - now) 
        hours, minutes = td.seconds// (3600), td.seconds// 60 % 60
        print(f"The token will expire in {hours} hours and {minutes} minutes.")
