import requests
from bs4 import BeautifulSoup
import html5lib
import pprint
url = "https://www.flipkart.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div')
#print(table)
quotes = []
for row in table.find_all('p'):
    print(row)
    quotes.append(row.get_text())

print(quotes)

