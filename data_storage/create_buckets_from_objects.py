import boto3

s3_resource = boto3.resource('s3')
first_bucket_name = 'bucket_name'
first_bucket = s3_resource.Bucket(name = first_bucket_name)
print(first_bucket_name)
# 'firstpythonbucket87fb9e33-fa52-40fc-af1c-a1636d852d26 us-east-1'

first_file_name = 'file_name'
first_object = s3_resource.Object(
    bucket_name = first_bucket_name, 
    key = first_file_name)

first_object_again = first_bucket.Object(first_file_name)
first_bucket_again = first_object.Bucket()

# there are three ways to upload a file to a bucket
# object instance, bucket instance, client

# using the object instance
first_object.upload_file(first_file_name)

# using the bucket instance
first_bucket.upload_file(Filename = first_file_name, Key=first_file_name)
# You have to enter the file name twice, first to id what the file is
# the other time to id how the key will store the file in the bucket

# downloading files from s3
s3_resource.Object(first_bucket_name, first_file_name).download_file(f'/tmp/boto_test/{first_file_name}')