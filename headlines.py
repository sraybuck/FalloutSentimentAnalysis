import requests
import bs4

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
payload = {'as_epq': 'Fallout 76', 'tbs':'cdr:1,cd_min:11/14/2018,cd_max:12/14/2018', 'tbm':'nws'}
r = requests.get("https://www.google.com/search", params=payload, headers=headers)

print(r.url)

soup = bs4.BeautifulSoup(r.text, 'lxml')

headlines = soup.select("div.g.card h3")

headlines_clean = []

for row in headlines:
    clean = row.text
    headlines_clean.append(clean)

print(headlines_clean)
