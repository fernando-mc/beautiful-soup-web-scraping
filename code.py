import requests
from pprint import pprint
from bs4 import BeautifulSoup

REDMOND_URL = 'http://livingwage.mit.edu/metros/13460'
CORVALLIS_URL = 'http://livingwage.mit.edu/metros/18700'

r = requests.get(CORVALLIS_URL)
data = r.text

print(data)
pprint(data)

soup = BeautifulSoup(data, 'html.parser')

print(soup.prettify())

table_data = soup.find_all('td')
table_data[0]
table_data[1] # This is what we want (The 1 Adult Living Wage)
table_data[2]
# Get Adult living wage

d = table_data[1]
type(d)
d = str(d)

# Clean up the data
d = d.replace(' ','') # Remove Spaces
d = d.replace('<td>','') # Remove starting HTML tag
d = d.replace('</td>','') # Remove closing HTML
d = d.replace('\n','') # Remove Newlines

print(d)

# Let's make this a function

def get_adult_living_wage(page_url):
    # Get page text
    data = requests.get(page_url).text
    # Turn it into soup
    soup = BeautifulSoup(data, 'html.parser')
    # Get what we assume is the (a)dult (l)iving (w)age
    alw = str(soup.find_all('td')[1])
    alw = alw.replace(' ','').replace('/','').replace('\n','').replace('<td>','')
    # Let's also get the location
    # location = str(soup.title).
    return alw

# Let's try it for redmond
get_adult_living_wage(REDMOND_URL)



# how do we get some more metraos