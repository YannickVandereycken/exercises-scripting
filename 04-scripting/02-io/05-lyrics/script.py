import sys
import re
import urllib
import json

artist=sys.argv[1]
title=sys.argv[2]
artist = re.sub(" ", "%20",artist)
title = re.sub(" ", "%20",title)

url = "https://api.lyrics.ovh/v1/{}/{}".format(artist,title)
print(url)
website = urllib.FancyURLopener({}).open(url)
print(website.read())

x = json.loads(website.read())
print(x['lyrics'])