import requests
from requests import get
from bs4 import BeautifulSoup  
import pandas as pd
import numpy as np
import urllib.request, urllib.error, urllib.parse
from time import sleep
from random import randint

url = "https://www.learncpp.com/"

headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

links = []

title_div = soup.find_all('a')

print("Reading Links..........")

for item in title_div:
    link = item.get('href')
    links.append(link)

links = links[7:]
links = list(filter(lambda a: a!=None, links))

print("Links Done Reading!")
print("Downloading the webpages.....")

i=0

for page in links:
    print("Downloading Page...",i)
    response = urllib.request.urlopen(page)
    webContent = response.read()
    file_name = 'a'+str(i)+'.html'
    f = open(file_name, 'wb')
    f.write(webContent)
    f.close
    i = i+1
    sleep(randint(2,10))

