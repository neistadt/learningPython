from bs4 import BeautifulSoup
import requests
import textwrap

r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
for section in soup.select('section.content-section > p'):
    print('\n'.join(textwrap.wrap(section.text.strip())), '\n')
