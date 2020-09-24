import requests
from bs4 import BeautifulSoup

url = '''
https://www.amazon.com/Rokinon-Ultra-Digital-Cameras-10M-C/dp/B00JD4TCR6/ref=sr_1_25?dchild=1&keywords=romania+wide+lens&qid=1598415641&sr=8-25'''

headers = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html')
title = soup.find(id='productTitle')
print(soup.prettify())
print(title)