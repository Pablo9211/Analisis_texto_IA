import PyPDF2
import download_files2 as dw

url1 = input("ingrese la url: ")
filename = input("ingrese nombre del archivo (poner .pdf): ")

dw.download(url1,filename)

pdffileobj = open(filename, 'rb')
pdfreader = PyPDF2.PdfReader(pdffileobj)
x = len(pdfreader.pages)
i = 0
while i<x:
    pageobj = pdfreader.pages[i]
    text = pageobj.extract_text()
    i= i+1

print(text)
with open("2.txt","w", encoding="utf-8") as file1:
    file1.writelines(text)
    file1.close()
