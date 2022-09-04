#!/usr/bin/python3

from os import system
from sys import argv

special_chars = dict()

special_chars['+'] = '%2B'
special_chars['#'] = '%23'
special_chars['&'] = '%26'

# Endpoint for querying
host_url = 'http://www.google.com/search?q='

def process_string(query: str) -> str: 
    # Replace special chars
    for char in special_chars.items():
        query = query.replace(char[0], char[1])
    # Replace spaces
    query = query.replace(' ', '+')
    return query

def googler():
    if len(argv) < 2:
        print('[ERROR] Required URL String.')
        return
    query = argv[1]
    google_query = process_string(query)
    url = host_url + google_query
    print(url)
    system(f'open {url}')

if __name__ == "__main__":
    googler()
