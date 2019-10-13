

from flask import Flask

app = Flask(__name__)

@app.route('/FLASK_BDDT/')

def home():
    return "Hello world!"

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
