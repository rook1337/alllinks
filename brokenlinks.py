from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib
import re
import requests 

def Find(link): 
  
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:http|https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,link)       
    return [x[0] for x in url] 




url="http://arksingh.heliohost.org/"

req = Request(url)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, 'html.parser')

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
    #page=requests.get(link)
    page=Find(str(link))
    if page is None:
        print("No")
    else:
        print("yes")

    print(url,link.get('href'))

    



      


#urlparse(url).netloc
#print(links)