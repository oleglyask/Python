
import requests
from bs4 import BeautifulSoup

url = 'https://codingnomads.github.io/recipes/'

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

# Search for links inside the container with class name = 'content is-normal'
links = soup.find( class_ = "content is-normal" ).find_all('a')

for link in links:
    if link.text.lower().find('leek') != -1:
        print(link.text)

