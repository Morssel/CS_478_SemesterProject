
import random
import string
import os
import boto3
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from PDF_parser import *
from Utilities import *
from Solr_query import *


ALLOWED_EXTENSIONS = set(['txt', 'pdf','doc','docx'])
process_file = ''

server_address = "http://localhost:8983/solr/"
core = "BDDT"
sq = Solr_query(server_address, core)

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
        r = ''
        if 'a_submit' in request.form:
            author_title_text = request.form['author_title_search']
            print(author_title_text)
            global sq
            r = sq.title_lookup(author_title_text)
            html_result = json2html.convert(r)
            new_file_name = os.path.join(app.config['TEMPLATE_FOLDER'], "result.html")
            with open(new_file_name, "w", encoding="utf-8") as f1:
                f1.write(html_result)
        elif 't_submit' in request.form:
            text_search = request.form['text_search']
            print(text_search)
            r = sq.content_lookup(text_search)

            html_result = json2html.convert(r)
            new_file_name = os.path.join(app.config['TEMPLATE_FOLDER'], "result.html")
            with open(new_file_name, "w", encoding="utf-8") as f1:
                f1.write(html_result)

        return render_template('result.html')

# need to do the content search and return the result
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

            # setup result string to be turned into a html file and stored on S3 bucket
            result = "<html>\n" +result+ "\n</html>"
            f = open("/tmp/"+web_link+".html","w+")
            f.write(result)
            f.close()

            session = boto3.Session(profile_name='zappa-project')  # If you only have one AWS account in you .aws credentials then this can be default
            # # Note that the profile "zappa-project" will only work on Joseph's machine as it is unique
            s3 = session.resource('s3')  
            s3.meta.client.upload_file('/tmp/'+web_link+'.html', 'zappabucketjktest', 'static/'+web_link+'.html', ExtraArgs={'ContentType': "text/html", 'ACL': "public-read"})
            txtURL = 'https://zappabucketjktest.s3.us-east-2.amazonaws.com/static/'+web_link+'.html'

            # get author and title data and weblink and write to file & post to the solr server
            author_text=''
            title_text=''

            if 'title_text' in request.form and request.form['title_text'] != 'Enter Title':
                title_text = request.form['title_text']
                print(title_text)
            if 'author_text' in request.form and request.form['author_text'] != 'Enter Author':
                author_text = request.form['author_text']
                print(author_text)
            http_link ="http://localhost:5000/FLASK_BDDT/PARSED/"+web_link + '.html'
            make_solr_json(http_link, author_text, title_text, filename, result)
            post_solr_update()

            return render_template('textfile.html', txtURL = txtURL )
            #return redirect('/FLASK_BDDT/PARSED/' + web_link + '.html')
        else:
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)

    return render_template('upload.html')



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
    app.run(debug=True)