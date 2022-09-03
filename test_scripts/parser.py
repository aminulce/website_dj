import PyPDF2
from func import aiParser
file = open('resume1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(file)
pageObj = pdfReader.getPage(0)
txt = pageObj.extractText()  
txtencode = txt.encode("ascii", "ignore")

txtdecode = txtencode.decode()  

pr = aiParser.get_degree(txtdecode)
  
print(pr)
  
  
  
  
  
  
# printing number of pages in pdf file
# print("Total number of pages in sample.pdf",pdfReader.numPages)
  
 
# creating a page object
# 



# extracting text from page
# print(txtdecode)
  
# closing the pdf file object
# file.close()