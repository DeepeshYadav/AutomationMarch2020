"""
pip install requests
pip install bs4
pip install html5lib
"""

import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://www.pyinstaller.org/"

raw_data = requests.get(url)

print(raw_data.content)
print(raw_data.status_code)
#(raw_data.text)

soup = BeautifulSoup(raw_data.content, 'html5lib')

all_links = soup.find('div')
print(all_links)

paragraph_data = soup.find('p')
print(paragraph_data)

#print(all_links)

text_data = []
link_data = []

for data in all_links.findAll('a'):
    link_data.append(data['href'])
    text_data.append(data.get_text())

print(text_data)
print(link_data)
