import argparse
from dataclasses import replace
import re,os
from pathlib import Path
#from PIL import Image

parser = argparse.ArgumentParser(prog='thumbnails')
parser.add_argument('files', nargs='+')
parser.add_argument('--size', default='64x64')
parser.add_argument('--pattern', default='%b-thumbail.%x')


# Parses sys.argv and stores parameters in args
args = parser.parse_args()

match = re.fullmatch(r'(\d+)x(\d+)', args.size)
w,h = match.groups()

print(args)
#print(w,h)

def getoutputname(file,pattern):
    path = Path(file)
    base = path.stem
    exten = path.suffix
    return pattern.replace('%b',base).replace('.%x',exten)

for file in args.files:
    print(getoutputname(file,args.pattern))