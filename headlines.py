import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import nltk
from nltk.corpus import stopwords

#method definition for tokenization later
def clean_tokens(a_list):
    #tokenize and clean list
    words = nltk.word_tokenize(a_list)
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words

#metadata so that google doesn't think I'm a robot
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
#the google query that im making
payload = {'as_epq': 'Fallout 76', 'tbs':'cdr:1,cd_min:11/14/2018,cd_max:12/14/2018', 'tbm':'nws'}
#actually going and talking to the website with the metadata and query
r = requests.get("https://www.google.com/search", params=payload, headers=headers)

#print url to verify its correct
print(r.url)

#create BeautifulSoup object out of the text from the requested site
soup = bs4.BeautifulSoup(r.text, 'lxml')

#select only the headlines in each google search result
base = soup.select("div.g.card h3")

#declare empty list where I'm going to put all the headlines
headlines = []

#loop to get rid of all html and keep only headline text
for row in base:
    clean = row.text
    headlines.append(clean)

#print to verify headlines are clean
print(headlines)

#empty list to store tokenized headlines
tokens = []

#loop to tokenize headlines by using clean_tokens method from earlier
for count, each in enumerate(headlines):
    clean = clean_tokens(headlines[count])
    tokens.append(clean)

#print to verify
for x in tokens:
    for y in x:
        print(y)
#create stopwords list from nltk and add fallout 76 as stopwords
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append("fallout")
stopwords.append('76')
stopwords.append("'fallout")

#print(stopwords)
filtered_sentence = []
for list in tokens:
    x = []
    for word in list:
        if word not in stopwords:
            x.append(word)
        if not x:
            filtered_sentence.append(x)

print(filtered_sentence, sep = "\n")

""""
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for count,line in enumerate(headlines):
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = headlines[count]
    results.append(pol_score)

print(*results, sep = "\n")
"""
