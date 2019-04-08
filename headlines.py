import requests
import bs4
import pandas as pd
import nltk
import csv
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
#print(headlines)

#empty list to store tokenized headlines
tokens = []

#loop to tokenize headlines by using clean_tokens method from earlier
for each in headlines:
    clean = clean_tokens(each)
    tokens.append(clean)

#print tokens to verify
#print('tokens =',tokens)

#create stopwords list from nltk and add fallout 76 as stopwords
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append("fallout")
stopwords.append('76')
stopwords.append("'fallout")

#remove stopwords from tokens
filtered = []
for list in tokens:
    x = []
    for word in list:
        if word not in stopwords:
            x.append(word)
    filtered.append(x)

#print to verify stopwords are gone
#print("filtered = ", filtered)

#declare empty list so I can put the tokens back into headlines without stopwords
combined = []

#put tokens back into headlines without stopwords
for list in filtered:
    combined.append(" ".join(list))

#import sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

#create sia object I think and then create empty list to put end results in
sia = SIA()
results = []

#analyze sentiment of each headline
for line in combined:
    pol_score = sia.polarity_scores(line)
    results.append(pol_score)

#print to verify
for i in results:
    print(i)
"""
#write sentiment analysis to csv file
with open('resultslist.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for dict in results:
        for key, value in dict.items():
            writer.writerow([key, value])
"""
