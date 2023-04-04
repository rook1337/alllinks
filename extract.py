import re

filename = "test.txt"

with open(filename, 'r') as file:
    data = file.read()
    
    # Use regex to find all domain names and subdomains
    domain_regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
    domain_names = re.findall(domain_regex, data)

    # Print the domain names
    for domain in domain_names:
        print(domain)

