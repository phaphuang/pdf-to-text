#ISO-8859-1
#utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import PyPDF2 as pypdf
import codecs

filename = 'DELTAT1.pdf'

with codecs.open(filename, 'rb') as f:

    pdfReader = pypdf.PdfFileReader(f)

    print("Total Page {}".format(pdfReader.numPages))

    num_pages = pdfReader.numPages
    count = 0
    text = ""

    #The while loop will read each page
    while count < 6:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText().encode('UTF-8')

    if text != "":
       text = text
       print(text)
