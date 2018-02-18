import requests
from bs4 import BeautifulSoup


def find_stories():
    r = requests.get('http://www.nyt.com')
    r.raise_for_status()
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    stories = []
    for story_heading in soup.find_all(attrs={'class': 'story-heading'}):
        stories.append(story_heading.text.replace("\n", " ").strip())

    return stories


if __name__ == '__main__':
    print('All the New York Time articles as of now: ')
    print('\n'.join(find_stories()))
