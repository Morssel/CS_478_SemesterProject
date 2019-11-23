
import random
import string
import os
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from PDF_parser import *
from Utilities import *


ALLOWED_EXTENSIONS = set(['txt', 'pdf','doc','docx'])

process_file = ''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def randomString(stringLength=15):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))





'''
@app.route('/FLASK_BDDT/')
def upload_form():
    return render_template('upload.html')
'''

@app.route('/FLASK_BDDT/')
def homepage():
    return render_template('index.html')


@app.route('/FLASK_BDDT/SEARCH/', methods=['GET', 'POST'])
def searchpage():
    if request.method == 'POST':
        if 'a_submit' in request.form:
            author_title_text = request.form['author_title_search']
            print(author_title_text)
        if 't_submit' in request.form:
            text_search = request.form['text_search']
            print(text_search)

    return render_template('search.html')



@app.route('/FLASK_BDDT/UPLOAD/', methods=['GET', 'POST'])
def upload_form():
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            global process_file
            process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result = tika_parse(process_file)
            web_link = randomString()
            new_file_name = os.path.join(app.config['PARSED_FOLDER']) + '/' + web_link + '.html'
            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write(result)
            return redirect('/FLASK_BDDT/PARSED/' + web_link + '.html')
        else:
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)

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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            global process_file
            process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result = tika_parse(process_file)
            web_link = randomString()
            new_file_name = os.path.join(app.config['PARSED_FOLDER'], web_link, ".html")

            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write(result)
            return redirect('/FLASK_BDDT/PARSED/'+web_link)
        else:
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)




@app.route('/FLASK_BDDT/PARSE_File')
def home():
    f_name = process_file
    result = tika_parse(f_name)
    return result

@app.route('/FLASK_BDDT/PARSED/<web_link>')
def get_stored_pages(web_link):
    f_name = os.path.join(app.config['PARSED_FOLDER'], web_link)
    with open(f_name, "r", encoding="utf-8") as f2:
        retrieve_txt=f2.read()
    return retrieve_txt


if __name__ == "__main__":
    app.run()