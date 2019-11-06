import os
import boto3
import re
import requests

from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from PDF_parser import *

ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

process_file = ''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# app is defined as "app = Flask(__name__, static_folder="/tmp")"
# @app.route('/FLASK_BDDT/')
@app.route('/')
def upload_form():
    return render_template('Upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.filename): # Successfully identified a file to upload
            filename = secure_filename(file.filename)
# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            s3 = boto3.client('s3') # New
            for bucket in s3.buckets.all():
                print(bucket.name)
            #s3.upload_file('/tmp/vin_qr_code.png', 'vin-generator-python-flask', 'static/vin_qr_code.png')
            #staticFilename = "static/" + filename 
            #s3.upload_file(filename, 'bddtprojectbucket', staticFilename)
            s3.upload_file('Test1.pdf', 'flaskfolder', 'Test1.pdf')
            flash('File successfully uploaded')
            global process_file
            #s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
            s3.download_file('bddtprojectbucket', 'static/Test1.pdf', 'Test1.pdf')
            #process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return redirect('/FLASK_BDDT/PARSE_File')
        else:
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)


@app.route('/FLASK_BDDT/PARSE_File')
def home():
    f_name = process_file
    #result = getTEXT(f_name)
    result = tika_parse(f_name)
    #new_str = strip_out_control_char(result)
    return result


if __name__ == "__main__":
    session = boto3.Session(profile_name='zappa-project')
    s3 = session.resource('s3') # New
    for bucket in s3.buckets.all():
        print(bucket.name)
    #App.run()