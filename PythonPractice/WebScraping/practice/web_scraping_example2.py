import requests
from bs4 import BeautifulSoup
import html5lib


url = "http://www.values.com/inspirational-quotes"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

print(soup.prettify())