import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse
from urlextract import URLExtract
import re
import sys
import os
from domains import domains_func
from termcolor import colored
from domains import sort_func
from domains import printsortdm


print(colored("""\
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
    ""","blue"))
parser = argparse.ArgumentParser()

f1 = open('alllinks.txt', 'r+')
f1.truncate(0)
f2 = open('domainsout.txt', 'r+')
f2.truncate(0)
f3 = open('domainsoutsort.txt', 'r+')
f3.truncate(0)
 # need '0' when using r+
#=========================================================
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


urls1=[]

#=========================================================


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
    #=========================================================
    extractor = URLExtract()
    urls = extractor.find_urls(str(getpage_soup))
    if not urls:
      x=1
    else:
      urls1.append(urls)


   # with open(r"C:\Users\DELL-7373\Documents\allscripts\hacking\alllinks\file.txt", "a") as file1: 
    # Writing data to a file 
    #  file1.writelines(str('\n'.join(flatten_list(urls1)))) 
    f = open(r"alllinks.txt", "w")
    f.write('\n'.join(flatten_list(urls1)))
    f.close()
    domains_func()
    sort_func()
    printsortdm()
    print(colored('Output file:- domainsout.txt and alllinks.txt', 'yellow','on_blue'))
    #=========================================================
    """for link in all_links:
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
           """
    
else:
    print("Error: --url not found in the command! Type --help for more info!")