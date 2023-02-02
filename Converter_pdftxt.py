import PyPDF2

pdffileobj = open('resonance.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(pdffileobj)
x = len(pdfreader.pages)
pageobj = pdfreader.pages[x - 1]
text = pageobj.extract_text()
print(text)
with open("2.txt","w", encoding="utf-8") as file1:
    file1.writelines(text)
    file1.close()
