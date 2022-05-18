import argparse
import re
import os

parser = argparse.ArgumentParser(prog='thumbnails')
parser.add_argument('location', nargs='+')
parser.add_argument('--minimum-size', type=int, help='only files whose size is at least `N` must be listed.')
parser.add_argument('--maximum-size', type=int, help='only files whose size is at most `N` must be listed.')
parser.add_argument('--no-directories', action='store_true')
parser.add_argument('--no-files', action='store_true')
parser.add_argument('--extension')
parser.add_argument('--contains')

args = parser.parse_args()

for file in os.listdir(args.location):

    os.path.getsize()
    if file.endswith(".txt"):
        if(args.no_directories):
            print(file)
        if(args.no_directories):
            print(os.path.join(args.location, ""))
        else:
            print(os.path.join(args.location, file))