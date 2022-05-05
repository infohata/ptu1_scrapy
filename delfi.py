from bs4 import BeautifulSoup
import requests


source = requests.get('https://delfi.lt/p').text
print(source)
