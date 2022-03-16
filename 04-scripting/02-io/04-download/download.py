import sys
import urllib

website = urllib.FancyURLopener({}).open(sys.argv[1])
print(website.read())