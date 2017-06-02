# Web text scraper, adapted from StackOverflow question. Uses CSV in case of adding extra stuff.
import requests
import csv
from bs4 import BeautifulSoup

url = "http://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))

with open('output.csv', 'ab') as f:
    writer = csv.writer(f)
    content = text.encode('utf-8')
writer.writerow([content])
