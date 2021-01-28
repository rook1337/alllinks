from urlextract import URLExtract
import os
from urllib.parse import urlparse
from termcolor import colored


def domains_func():
  extractor = URLExtract()
  with open(r"alllinks.txt", "r") as infile:
      for line in infile:
          for url in extractor.gen_urls(line):
              domain = urlparse(url).netloc
              if domain =="":
                  f = open(r"domainsout.txt", "a")
                  f.write(url+"\n")
                  f.close()
                  
              else:
                  f = open(r"domainsout.txt", "a")
                  f.write(domain+"\n")
                  f.close()


def sort_func():
    lines_seen = set() # holds lines already seen
    with open(r"domainsoutsort.txt", "w") as output_file:
	    for each_line in open(r"domainsout.txt", "r"):
	        if each_line not in lines_seen: # check if line is not duplicate
	            output_file.write(each_line)
	            lines_seen.add(each_line)


def printsortdm():
    f = open(r"domainsoutsort.txt", "r")
    print(colored(f.read(),"green"))
