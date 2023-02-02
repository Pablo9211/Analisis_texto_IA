import requests


def download_file(url):
    r = requests.get(url, stream=True)
    chunk_size = 2000
    with open('/home/juan/Juan Pablo/Analisis_texto_IA/metadata.pdf', 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    return "succes"

url = input("Ingrese el link a descargar: ")
download_file(url)