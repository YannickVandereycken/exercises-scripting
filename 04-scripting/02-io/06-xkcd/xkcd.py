import imp
import sys
import re
import urllib.request
import json
#from pil import Image

if(len(sys.argv) == 1):
    url = 'https://xkcd.com/info.0.json'
else:
    number=sys.argv[1]
    url = f'https://xkcd.com/{number}/info.0.json'
    #url = 'https://xkcd.com/{}/info.0.json'.format(number)

print(url)
website = urllib.request.urlopen(url)
#website = urllib.FancyURLopener({}).open(url)
#print(website.read())



x = json.loads(website.read())
print('number: ',x['num'])
print('day: ',x['day'])
print('month: ',x['month'])
print('year: ',x['year'])
print('safe title: ',x['safe_title'])
print('transcript: ',x['transcript'])
print('img: ',x['img'])
print('alt title: ',x['alt'])

#Image.open(x['img']).show()