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
@app.route('/FLASK_BDDT/')
#@app.route('/')
def upload_form():
    return render_template('index.html')

#@app.route('/', methods=['POST'])
@app.route('/', methods=['POST', 'GET'])
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
            session = boto3.Session(profile_name='zappa-project')  # If you only have one AWS account in you .aws credentials then this can be default
            # Note that the profile "zappa-project" will only work on Joseph's machine as it is unique
            s3 = session.resource('s3')
            s3.meta.client.upload_file(filename, 'zappabucketjktest', filename)
# !!! Need to change the filename in S3 so it is not the same as when it was uploaded, to prevent duplicate naming
            #s3.meta.client.upload_file('Test1.pdf', 'zappabucketjktest', 'hello.pdf')
            flash('File successfully uploaded')
            global process_file
            process_file = s3.meta.client.download_file('zappabucketjktest', filename, filename)
            #process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #return redirect('/FLASK_BDDT/PARSE_File')
            #return home()
            return "made it to inside the if"
        else:
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)
    return render_template('index.html') #every flask function needs a return, the above returns are encapsulated in if statements so this return is basically an else return


#@app.route('/FLASK_BDDT/PARSE_File')
#@app.route('/')
def home():
    print("redirect to home() parsing")
    f_name = process_file
    #result = getTEXT(f_name)  // getTEXT accepts PDF inputs
    result = tika_parse(f_name)
    #new_str = strip_out_control_char(result)
    return result


if __name__ == "__main__":
    app.run()