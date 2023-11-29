import boto3
from boto3_practice import create_temp_file

first_bucket = 'bucket_name'
file = create_temp_file(400, 'second_file.txt', 's')
# print(file)

s3_resource = boto3.resource('s3')
bucket_obj = s3_resource.Object(first_bucket, file)
# to set group (everyone) permissions to read-only
bucket_obj.upload_file(file, ExtraArgs = {
    'ACL':'public-read'})

# to verify the bucket acl
bucket_obj_acl = bucket_obj.Acl()

# to verify the granted permissions on the bucket
bucket_obj_acl.grants

# change bucket permissions to private
response = bucket_obj_acl.put(ACL = 'private')

# add encryption
file3 = create_temp_file(300, 'file3.txt','t')
bucket = boto3.resource('s3')
bucket_obj = bucket.Object(first_bucket, file3)
bucket_obj.upload_file(file3, ExtraArgs={
                         'ServerSideEncryption':'AES256'})
bucket_obj.server_side_encryption
# 'AES256'


