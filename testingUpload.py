import logging
import boto3
from botocore.exceptions import ClientError
import aws



#def upload_file(file_name, bucket, object_name=None):
    # """Upload a file to an S3 bucket

    # :param file_name: File to upload
    # :param bucket: Bucket to upload to
    # :param object_name: S3 object name. If not specified then file_name is used
    # :return: True if file was uploaded, else False
    # """
#file_name = 'Test1.pdf'
#bucket = 'zappabucketjktest'
#object_name = 'static/test.pdf'

    # If S3 object_name was not specified, use file_name

    # Upload the file
# session = boto3.Session(profile_name='zappa-project')
# credentials = session.get_credentials()
# credentials = credentials.get_frozen_credentials()
# access_key = credentials.access_key
# secret_key = credentials.secret_key

# print("found " + access_key + " and  " + secret_key)

# ACCESS_KEY = "AKIAJFTWFLZDBARUDPAA"
# SECRET_KEY = "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"
# SESSION_TOKEN = aws.sts.GetSessionToken()

# client = boto3.client(
#     's3',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
#     aws_session_token=SESSION_TOKEN,
# )


# s3 = session.resource('s3') # New
# #s3 = boto3.client('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
# #s3_client = boto3.client('s3')
# bucket.upload_file("Test1.pdf", "zappabucketjktest", "Test1.pdf")
# print('finished running')

session = boto3.Session(profile_name='zappa-project')
s3 = session.resource('s3')
s3.meta.client.upload_file('Test1.pdf', 'zappabucketjktest', 'hello.pdf')