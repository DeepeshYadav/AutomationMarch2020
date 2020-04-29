import requests
import bs4
import html5lib

url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"

data = requests.get(url)

print(data.content)

for value in data.content:
    print(value)