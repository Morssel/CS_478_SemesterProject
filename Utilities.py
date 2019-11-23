import os
from app import app
import subprocess

# Utility functions:
# write to file a list of web links

# random string generator

#

# idea: need to add read and write a string to file
# after parsing, store the result to a string
#


def make_solr_json(web,author,title,fname,content):
    s1 = '{ "Web_BDDT":"' + web + '",'
    s2 = '"Author_BDDT":"' + author + '",'
    s3 = '"Title_BDDT":"' + title + '",'
    s4 = '"File_BDDT":"' + fname + '",'
    s5 = ' "Content_BDDT":"' + content + '"'
    s_end = '}'
    str =  s1 + s2 + s3 + s4 + s5 + s_end
    filename='update.json'
    process_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(process_file, "w", encoding="utf-8") as f:
        f.write(str)

make_solr_json("http://testing23.com","John Doe","My test title","Test.pdf","Once upone a time....")

def post_solr_update():
    command='java -Dc=BDDT -Dauto -jar C:/Users/alber/Software/solr-7.7.2/bin/post.jar C:/Users/alber/CS/SW_Eng/BDDT/CS_478_SemesterProject/Uploads/update.json'
    message = subprocess.call(command, shell=True)