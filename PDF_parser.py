
# Install PyPDF4
# run "pip3 install PyPDF4"

from PyPDF4 import PdfFileReader
import re
from tika import parser


#f_name='Test1.pdf'

f_name='MidTermStudyGuide.pdf'

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

    #text = text.replace("\n", "<br />\n")
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


fname='str_test4.txt'
with open(fname, "w", encoding="utf-8") as f:
    f.write(result)


fname='str_test5.html'
with open(fname, "w", encoding="utf-8") as f:
    f.write(result)


result2 = result.replace("\n", "<br />\n")

fname='str_test5.html'
with open(fname, "w", encoding="utf-8") as f:
    f.write(result2)


def tika_parse(f_name):
    # Parse data from file
    file_data = parser.from_file(f_name)
    # Get files text content
    text = file_data['content']
    text = text.replace("\n", "<br />\n")
    return text

a=tika_parse(f_name)