#!/usr/bin/python3
"""
    This script sends a get request for commits to the github api
    The 'sha' and 'author' of every commit is printed in custom format
"""
if __name__ == '__main__':
    from requests import get
    from sys import argv
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    foo = get(url)
    foo = foo.json()
    for i in range(10):
        sha = foo[i].get('sha')
        author = foo[i].get('commit').get('author').get('name')
        print(f'{sha}: {author}')
