import boto3
import configparser
import pandas as pd
from pathlib import Path

config = configparser.ConfigParser()
config.read('config.ini')

S3Bucket = config['default']['S3Bucket']
SourceKey = config['default']['SourceKey']
TargetKey = config['default']['TargetKey']
Filename = Path(config['default']['SourceKey']).stem

s3_client = boto3.client('s3')

print ("Downloading File...")
# Download file
s3_client.download_file(
    S3Bucket,
    SourceKey,
    Filename
    )

print ("Converting to parquet...")
#Transform to parquet
fn = Filename + ".parquet"
df = pd.read_csv(Filename)
df.to_parquet(fn)


print ("Uploading to S3...")
# Upload file
object_name = TargetKey + fn
response = s3_client.upload_file(
    fn,
    S3Bucket,
    object_name
    )

print (response)
