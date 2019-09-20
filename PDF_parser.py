
# Install PyPDF4
# run "pip3 install PyPDF4"

from PyPDF4 import PdfFileReader

f_name='Mod 1 Part A.pdf';
with open(f_name, 'rb') as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()

num_pages = pdf.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdf.getPage(count)
    count +=1
    text += pageObj.extractText()


pdfFileObj = open(f_name, 'rb')
pdfReader = PdfFileReader(pdfFileObj)
count = 0
text = ""
num_pages = pdfReader.numPages

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    temp_text = pageObj.extractText()
    text += temp_text
    count += 1

print(text)