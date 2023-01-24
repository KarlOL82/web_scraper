import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.ml'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

