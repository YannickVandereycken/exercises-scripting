import sys
import re
import urllib.request

def match(string):
    return re.fullmatch('^P.*on$',string)