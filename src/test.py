import requests


url = ''
proxies = {
    'http' : 'http://127.0.0.1:5001'
}

res = requests.get(url, proxies=proxies)