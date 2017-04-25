from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from urllib.request import urlopen
from bs4 import BeautifulSoup

fp = open('uf_salaries.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.

f = open("salaries.txt", "a")

for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):

            f.write(str(lt_obj.get_text()) + "\n")

            #liberal arts info pgs 323-364

f.close()

# def save(lst):
#     i = 0   # set to 0 but never changes
#     while i < len(lst):
#         txtfile = "enegep"+str(i)+".txt" #enegep is like the identifier of the files
#         artigo = convert_pdf_to_txt(list[0])
#         with open(txtfile, "w") as textfile:
#             textfile.write(article)
#             i += 1 # you need to  increment i
