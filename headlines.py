import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import nltk

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
payload = {'as_epq': 'Fallout 76', 'tbs':'cdr:1,cd_min:11/14/2018,cd_max:12/14/2018', 'tbm':'nws'}
r = requests.get("https://www.google.com/search", params=payload, headers=headers)

print(r.url)

soup = bs4.BeautifulSoup(r.text, 'lxml')

base = soup.select("div.g.card h3")

headlines = []

for row in base:
    clean = row.text
    headlines.append(clean)

print(headlines)

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []
count = 0

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = headlines[count]
    count = count + 1
    results.append(pol_score)

pprint(results)

df = pd.DataFrame.from_records(results)
df.head()
