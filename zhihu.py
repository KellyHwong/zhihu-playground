# encoding=utf-8
# Author: kellyhwong
# Date: 2018.4.25

# ReadMe.md
# If the zhihuer set that he/she cannot be touched outsided the site
# his/her values of following/followers cannot be obtained
# To deal with, a simulated logging in must be implemented

import requests
import collections
from bs4 import BeautifulSoup
import os

DEF_DEBUG = 0

# private config
def read_config(config_file="private.conf"):
    _dict = collections.OrderedDict()
    with open(config_file, 'r') as f:
        for line in f:
            # print(line)
            # print(line.strip(os.linesep).split(' '))
            if len(line.strip().split(' ')) == 2:
                [key, value] = line.strip().split(' ')
                _dict[key] = value
    return _dict

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def main():
    profiles = read_config()
    items = list(profiles.items())
    target_profile = items[0][1]
    html_doc = download_page(target_profile).decode('utf-8')
    # with open(filename, 'w') as f:
        # print(html_doc, file=f)
    soup = BeautifulSoup(html_doc,"lxml")
    values = soup.find_all("strong", {"class", "NumberBoard-itemValue"})
    # the first one is following
    print("follwing: " + values[0].string);
    # the second one is followers
    print("followers: " + values[1].string);

if __name__ == '__main__':
    main()
