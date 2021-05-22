import boto3
from dotenv import dotenv_values
import json

config = dotenv_values(".env")


client = boto3.client(
    's3',
    aws_access_key_id=config["AWS_ACCESS_KEY"],
    aws_secret_access_key=config["AWS_SECRET_KEY"],
    region_name=config["REGION"]
)   


response = client.list_objects(
    Bucket=config["S3_BUCKET"],
    
)

objects = response["Contents"]

musicNames = []

for key in objects:
    musicNames.append(key["Key"])

result = {"result": musicNames}

jsonresult = json.dumps(result)

print(jsonresult)