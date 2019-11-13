from flask import Flask

#UPLOAD_FOLDER = 'C:/wamp64/www/FLASK_BDDT/Uploads'
#UPLOAD_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/Uploads'
UPLOAD_FOLDER = '/Users/cph/Documents/School/CS_478_SemesterProject/UploadFolder'
# app = Flask(__name__) # <- original
app = Flask(__name__, static_folder="/tmp")
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024