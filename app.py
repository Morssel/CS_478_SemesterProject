from flask import Flask


UPLOAD_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/Uploads'
PARSED_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/PARSED'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PARSED_FOLDER'] = PARSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024