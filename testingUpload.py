import logging
import boto3
from botocore.exceptions import ClientError
import aws
import os
import re
import requests
import PyPDF2

from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from PDF_parser import *

def decodeFile():
    #theFile = open('downloadedfile.pdf', 'rb')
    # pdfReader = PyPDF2.PdfFileReader(theFile)
    # pageObj = pdfReader.getPage(2)
    # print(pageObj.extractText())
    # theFile.close()
    # return pageObj.extractText()
    # #return 'its working'
    # #print("redirect to home() parsing")
    #f_name = process_file
    process_file = os.path.join(app.config['UPLOAD_FOLDER'], "example.pdf")
    #process_file = 
    f_name = process_file
    # # #result = getTEXT(f_name)  // getTEXT accepts PDF inputs
    result = " "
    result = tika_parse(f_name)
    if result == " ":
        result = "no value"
    # # #new_str = strip_out_control_char(result)
    # #myString = "this is a string for sure"
    #return "The book is %s " % (result)
    print(type(result))
    #print(result)

if __name__ == "__main__":
    decodeFile()

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

# session = boto3.Session(profile_name='zappa-project')
# s3 = session.resource('s3')
# s3.meta.client.upload_file('Test1.pdf', 'zappabucketjktest', 'hello.pdf')