import requests
from bs4 import BeautifulSoup

# the url where we get the information from
url = 'https://hooper.link/contact'

# Fetching the content of the URL
response = requests.get(url)

# Parsing the content with BeautifulSoup
# this just basically means, getting a version of the website above, in memory
# (the computer visualises the website in its head)
soup = BeautifulSoup(response.text, 'html.parser')

# next we search our in memory website, 
# finding all 'a' tags and storing them in a variable 'a_tags'
a_tags = soup.find_all('a')

# we declare our value here - then the loop will (hopefully!) set it
our_final_value_from_the_site = None

# we now loop through all 'a' tags
for tag in a_tags:

  # the link part that we are looking for is in the 'href' part
  # of an a tag = so we get that
  href = tag.get('href')

  # we want the twitter url in our <a> tag - so look for one that has it in it
  if 'twitter' in href:
    # if it is, we print it

    # we want the last part of the href - so we split it by '/' and get the last part
    # (the [-1] means the last part)
    href = href.split('/')[-1]

    # set our final value to the href
    our_final_value_from_the_site = href

# print our final value
print(our_final_value_from_the_site)