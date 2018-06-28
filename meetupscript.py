#meetupapisjamilla
import requests
import pprint

current_url = "http://api.meetup.com/2/members?group_urlname=NAMEOFTHEGROUPHERE&fields=name&key=TOKENHERE"

while True:
    print 'Requesting %s' % current_url
    response = requests.get(current_url)
    data = response.json()

    for user in data["results"]:
        name = user["name"]
        link = user["link"]
        city = user["city"]
        joined = user["joined"]



        print '%s,%s,%s,%s' % (name, city, link, joined)

    meta = data["meta"] 
    if "next" in meta and meta["next"]:
        current_url = meta["next"]
    else:
        break
