import requests


def download_content(url):
    res = requests.get(url)
    return res.text
