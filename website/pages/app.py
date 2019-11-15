from flask import Flask

#UPLOAD_FOLDER = 'C:/wamp64/www/FLASK_BDDT/Uploads'
UPLOAD_FOLDER = 'C:/Users/jcand/Documents/websiteforbddt/website/pages'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024