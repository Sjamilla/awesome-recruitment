# meetup api scraping from terminal, created by Sjamilla van der Tooren
import pandas as pd
import requests

current_url = "http://api.meetup.com/2/members?group_urlname=NAMEOFTHEGROUPHERE&fields=name&key=TOKENHERE"

while True:
    print 'Requesting %s' % current_url
    response = requests.get(current_url)
    data = response.json()
    print 'Creating data frame'
    df = pd.DataFrame(data["results"], columns = ["name", "city", "link", "joined"])
    print 'writing to output.csv'
    df.to_csv('output.csv', encoding='utf-8-sig')

    meta = data["meta"]
    if "next" in meta and meta["next"]:
        current_url = meta["next"]
    else:
        break
