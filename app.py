from flask import Flask


#UPLOAD_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/Uploads'
#PARSED_FOLDER = 'C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/PARSED'
UPLOAD_FOLDER = '/Users/cph/Documents/School/secondSemProj/PARSED'
PARSED_FOLDER = '/Users/cph/Documents/School/secondSemProj/Uploads'

app = Flask(__name__, static_folder="/tmp")
#app = Flask(__name__)
#app.secret_key = "secret key"
app.secret_key = "OnZ0lPYxSVMcpC0CAOmEpKv185y0Ls/82G7PPZO+"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PARSED_FOLDER'] = PARSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024