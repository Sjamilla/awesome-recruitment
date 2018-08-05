# meetup api scraping from terminal, created by Sjamilla van der Tooren
import pandas as pd
import requests
import datetime


now = datetime.datetime.now()

group_name = 'NAMEOFTHEGROUPHERE'
api_key = 'TOKENHERE'


current_url = "http://api.meetup.com/2/members?group_urlname=" + group_name + "&fields=name&key=" + api_key

while True:
    print 'Requesting %s' % current_url
    response = requests.get(current_url)
    data = response.json()
    df = pd.DataFrame(data["results"], columns = ["name", "city", "link", "joined"])
    print 'Writing to csv'
    df.to_csv(group_name + '-' + now.strftime("%d-%m-%Y") + '.csv', encoding='utf-8-sig', mode = 'a')

    meta = data["meta"]
    if "next" in meta and meta["next"]:
        current_url = meta["next"]
    else:
        break
