import boto3
from boto3_practice import copy_to_bucket

# bucket and file context
first_bucket_name = 'from_bucket'
second_bucket_name = 'to_bucket'
file_name = 'file_to_move'
s3_resource = boto3.resource('s3')

# function to move files between buckets
copy_to_bucket(s3_resource,first_bucket_name,second_bucket_name,file_name)

# delete file from the from the bucket (is successful, will return a 204 response code)
s3_resource.Object(first_bucket_name, file_name).delete()
