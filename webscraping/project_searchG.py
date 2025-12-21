# step 1:  get the search page
import requests, sys, webbrowser, bs4
from googlesearch import search

# 1. Define a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print('Searching...') 

# step 2: find all results
query = ''.join(sys.argv[1:])
link_elems = list(search(query, num_results=5))
print('finding all results')


# step 3: open web browsers for each result

if(len(link_elems) == 0):
    print('No results found.')
    
else:
    num_open = min(5, len(link_elems))
    for i in range(num_open):
        url_to_open = link_elems[i]
        print('Opening', url_to_open)
        webbrowser.open(url_to_open)
        print('Open Browser')
