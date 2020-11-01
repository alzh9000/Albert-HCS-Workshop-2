# Web scrape the Google results for the Ivy League colleges to compare what articles and websites are saying about each one's research achivements and papers (to see what kind of work is accomplished at each school). Save the webpages to html files stored in this repo too.

import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

ivy = ["Brown University", "Columbia University", "Cornell University", "Dartmouth College",
       "Harvard University", "University of Pennsylvania", "Princeton University", "Yale University"]

for school in ivy:
    text = school + " research papers"
    text = urllib.parse.quote_plus(text)

    url = 'https://google.com/search?q=' + text

    response = requests.get(url)

    with open(school + '.html', 'wb') as f:
        f.write(response.content)
    webbrowser.open(school + '.html')

    soup = BeautifulSoup(response.text, 'html.parser')

    for g in soup.find_all(class_='BNeawe vvjwJb AP7Wnd'):
        print(g.get_text())
        print('---')
