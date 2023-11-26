import boto3
from boto3_practice import create_bucket


s3_resource = boto3.resource('s3')
first_bucket_name, first_bucket_response = create_bucket(
        # s3 name must be all lowercase 
        bucket_prefix = 'firstpythonbucket',
        s3_connection = s3_resource.meta.client)