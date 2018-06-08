import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    manager = PDFResourceManager()
    codec = 'utf-8'
    caching = True
    output = StringIO()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    convertedPDF = output.getvalue()
    print(convertedPDF)

    infile.close()
    converter.close()
    output.close()
    return convertedPDF

text = convert('EICT1-sub.pdf')
print(text)
