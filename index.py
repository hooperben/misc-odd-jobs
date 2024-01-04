import requests
from bs4 import BeautifulSoup

# the url where we get the information from
url = 'https://hooper.link/contact'

# Fetching the content of the URL
response = requests.get(url)

# Parsing the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all 'a' tags and storing them in a variable 'a_tags'
a_tags = soup.find_all('a')

# loop through all 'a' tags or using them as needed
for tag in a_tags:
  href = tag.get('href')  # Getting the href attribute of the tag
  if href:  # Making sure href is not None
    print(href)