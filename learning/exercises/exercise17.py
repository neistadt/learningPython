import requests
from bs4 import BeautifulSoup

print('All the New York Time articles as of now: ')
r = requests.get('http://www.nyt.com')
r.raise_for_status()
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
for story_heading in soup.find_all(attrs={'class': 'story-heading'}):
    print(story_heading.text.replace("\n", " ").strip())
