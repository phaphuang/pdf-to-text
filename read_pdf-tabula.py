#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2 as pypdf
import codecs

filename = 'DELTAT1.pdf'

pdfFileObj = open(filename, 'rb')
pdfReader = pypdf.PdfFileReader(pdfFileObj)

print("Total Page {}".format(pdfReader.numPages))

num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < 6:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text

print(text.decode('unicode_escape').encode('utf-8'))
