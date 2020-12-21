import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse


print("""\
                                  ##########
                               ################
                            #######%      ######
                          ########          ######
                        #######%            ######
                       ######   ###       #######
                      #####  #######   ########
                       ##  #######   #######%
              ######%   ########  ########
           #########  #######  ########%
         #######%  ########   &#####&
      ########   #######  ##
    #######%   ####### &#####
  #######       %##   ######
 #####%            ########
 ######          #######%
  #######    #########
    %##############%
       ##########
      Alllinks v1.1
    """)
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--url", "-u", help="Set the URL e.g- alllinks.py -u https://www.google.com")
parser.add_argument("--noise", "-n", help="Remove unnecessary domains e.g- alllinks.py -u https://www.google.com -n 'twitter.com,google.com'")
# Read arguments from the command line
args = parser.parse_args()
if args.url:
    getpage= requests.get(str(args.url))
    getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
    all_links= getpage_soup.findAll('a')
    domains=[]
    for link in all_links:
        #print (link.get('href'))
        
        if any(urlparse(link.get('href')).netloc in s for s in domains):
            x=0
        else:
            if args.noise:
                noiselist=args.noise.split(",")
                if any(urlparse(link.get('href')).netloc in nn for nn in noiselist):
                    x=0
                else:
                    domains.append(urlparse(link.get('href')).netloc)
            else:
                domains.append(urlparse(link.get('href')).netloc)
           
    
    print("\n".join(domains))
else:
    print("Error: --url not found in the command! Type --help for more info!")