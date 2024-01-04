import requests
from bs4 import BeautifulSoup

# the url where we get the information from
url = 'https://hooper.link'

# Fetching the content of the URL
response = requests.get(url)

# Parsing the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding the div with id="1234" and storing it in variable 'tester'
tester = soup.find('div', id='__next')

# Printing or using the 'tester' variable as needed
print(tester)