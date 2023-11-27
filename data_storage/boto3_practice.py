import boto3
import uuid

# clients return a dictionary response that requires parsing
# s_client = boto3.client('s3')

# will parse the dictionary 
# s3_resource = boto3.resource('s3')

# create an S3 bucket


def create_bucket_name(bucket_prefix):
    # the generated bucket name must be between 3 and 63 characters
    return ''.join([bucket_prefix, str(uuid.uuid4())])

# print(create_bucket_name('test_name'))

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
            Bucket = bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket = bucket_name, 
            CreateBucketConfiguration = {
                'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

# create temp file to push to s3
def create_temp_file(size, file_name, file_context):
    # joining a empty sring to a list, casted to a string, to the file name
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]),file_name])
    with open(random_file_name, 'w') as f:
        # multiple f by the size parameter within the call
        f.write(str(file_context) * size)
    return random_file_name

# copy file between buckets
def copy_to_bucket(s3_connection, from_bucket, to_bucket, file_name):
    copy_source = {
        'Bucket': from_bucket,
        'Key': file_name
    }
    s3_connection.Object(to_bucket, file_name).copy(copy_source)