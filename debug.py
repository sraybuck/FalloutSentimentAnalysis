import requests
import bs4
import pandas as pd
import nltk
import csv
import time
from nltk.corpus import stopwords

def create_nextsoup(url):
    #header to identify myself when scraping so google doesnt flag me as a robot
    headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        
    #actually going and talking to the website with the header and query
    r = requests.get(url, headers=headers)

    #create BeautifulSoup object out of the text from the initial request
    soup = bs4.BeautifulSoup(r.text, 'lxml')

    return soup

def next_page_url(soup_object):
    #select anchor tags for next page
    link = soup_object.select("#pnnext")

    #get the url from the anchor tag
    for i in link:
        url = i.get('href')


    #add google site base to url
    url = "https://www.google.com" + url
    print("next = ", url)
    return url

url = "https://www.google.com/search?as_epq=Fallout+76&tbs=cdr%3A1%2Ccd_min%3A11%2F14%2F2018%2Ccd_max%3A12%2F14%2F2018&tbm=nws"

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
    #actually going and talking to the website with the header and query
r = requests.get(url, headers=headers)
print(r.url)
time.sleep(10)
#create BeautifulSoup object out of the text from the initial request
soup = bs4.BeautifulSoup(r.text, 'lxml')

new_url = next_page_url(soup)
soup = create_nextsoup(new_url)
file = open("testdebug.html", "w")
file.write(str(soup))

time.sleep(10)
new_url = next_page_url(soup)
soup = create_nextsoup(new_url)
file1 = open("testdebug1.html", "w")
file1.write(str(soup))
