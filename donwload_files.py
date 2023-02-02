import requests


def download_file(url):
    r = requests.get(url, stream=True)
    chunk_size = 2000

    with open('resonance.pdf', 'wb') as fd:

        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    return "succes"

url = input("Ingrese el link a descargar: ")
##https://link.springer.com/content/pdf/10.1007/s12517-021-06624-3.pdf?pdf=button
download_file(url)