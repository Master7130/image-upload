import boto3

s3 = boto3.resource('s3')

# Create s3 bucket
s3.create_bucket(Bucket='image-upload-main')

# Configurate location
# s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
#     'LocationConstraint': 'us-east-1'})