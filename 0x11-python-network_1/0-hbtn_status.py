#!/usr/bin/python3
# This script will fetch intra.hbtn.io/status
import urllib.request

if __name__ == '__main__':

    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        readpg = response.read()
        utf8 = readpg.decode('utf-8')
    print('Body response:')
    print('\t- type: {}'.format(type(readpg)))
    print('\t- content: {}'.format(readpg))
    print('\t- utf8 content: {}'.format(utf8))
