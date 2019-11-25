from flask import Flask


UPLOAD_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/Uploads'
PARSED_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/PARSED'
TEMPLATE_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/templates'
TEMP_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/tmp'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PARSED_FOLDER'] = PARSED_FOLDER
app.config['TEMPLATE_FOLDER'] = TEMPLATE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TEMP_FOLDER'] = TEMP_FOLDER