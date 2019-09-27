
# Install PyPDF4
# run "pip3 install PyPDF4"

from PyPDF4 import PdfFileReader
import re


f_name='Test1.pdf'

# This function grabs the string from a pdf file
def getTEXT(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    count = 0
    text = ""
    num_pages = pdfReader.numPages

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        temp_text = pageObj.extractText()
        text += temp_text
        count += 1
        #print(text)

    return text

# This function strips out the control character
def strip_out_control_char(input):
    regex = re.compile(r'[\n\r\t]')
    return regex.sub(" ", input)

result = getTEXT(f_name)
new_str= strip_out_control_char(result)
#


# Program to show various ways to read and
# write data in a file.
fname='str_test.txt'
with open(fname, "w", encoding="utf-8") as f:
    f.write(new_str)

fname='str_test.html'
with open(fname, "w", encoding="utf-8") as f:
    f.write(new_str)

fname='str_test2.html'
with open(fname, "w", encoding="utf-8") as f:
    f.write(result)
