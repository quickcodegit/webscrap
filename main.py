import requests
from bs4 import beautifulSoup as bs

# Load webpage content
r = requests.get("Web Url")

# Convert to a beautiful soup object
soup = bs(r.content)

# Print out our html
print(soup.prettify())

# TODO: Start using Beautiful Soup to Scrape

# find and find_all
first_header = soup.find("h2")
print(first_header)
headers = soup.find_all("h2")
print(headers)

# Pass a list of elements to look for
headers_list = soup.find(["h1","h2"])
print(headers_list)

# You can pass in attribute to the find/find_all function