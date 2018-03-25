#Under MIT Open Source Liscence
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
#PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
#FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#Beautiful Soup Implementation - Used with permission from github.com/fernando-mc/beautiful-soup-web-scraping
#Living wage data collected from http://livingwage.mit.edu/. 

import requests
from pprint import pprint
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats




WAGE_URL = 'http://livingwage.mit.edu/'

r = requests.get(WAGE_URL)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

state_class = "states list-unstyled row"

print(soup.prettify())


states = []
states_links = []

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

#list of all the states -- 

for tag in soup.findAll('ul',{'class':state_class}):
    for li in tag.findAll('li'):
        states.append(li.text.replace(' ','').replace('\n',''))

for tag in soup.findAll('ul',{'class':state_class}):
    for a in tag.findAll('a'):
        print(a['href'])
        states_links.append((a['href']).replace(' ','').replace('\n',''))
        
state_living_wages = []

for i in range((len(states_links))):
    state_link = "http://livingwage.mit.edu"+str(states_links[i].replace('/locations',''))
    print('state_link: '+state_link)
    print("at state: "+str(states[i]))
    state_living_wages.append(get_adult_living_wage(state_link))

h = []
h = state_living_wages
for i in range(len(h)):
    print(type(h[i]))
    h[i]  = h[i].replace('$','')
    print(h[i])
h = list(map(float, h))
h = sorted(h)

fit = stats.norm.pdf(h, np.mean(h), np.std(h))

plt.plot(h,fit)

#pl.hist(h,normed=True)

plt.show()






# # Let's try it for redmond
# get_adult_living_wage(REDMOND_URL)