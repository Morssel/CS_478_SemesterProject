import os
import boto3
from flask import Flask, render_template, request
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
    s3 = boto3.client('s3') # New
    s3.upload_file('/tmp/vin_qr_code.png', 'zappabucketjktest', 'static/vin_qr_code.png') # New
    return render_template('upload.html')


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
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File successfully uploaded')
            global process_file
            process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
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
    app.run()