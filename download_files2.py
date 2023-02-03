import urllib.request


def download(url,namefile):

    urllib.request.urlretrieve(url, namefile)


