import urllib.request


def download(url,namefile):
    ''' esta funcion es para descargar archivos y recibe como variables
        la url y el nombre de el archivo ( tener en cuenta enviar el nombre del archivo finalizado con .pdf)
    '''
    urllib.request.urlretrieve(url, namefile)


