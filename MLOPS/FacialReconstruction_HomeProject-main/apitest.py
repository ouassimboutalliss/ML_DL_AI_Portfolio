import requests
import glob
import os

p = '/Ongeziene_Faces/im.jpg'
foto = open(p, 'rb')

url = "http://127.0.0.1:8000/predict/test" # url api of app

res = requests.post(url=url, file=foto)
print(res.status_code)
print(res.text)