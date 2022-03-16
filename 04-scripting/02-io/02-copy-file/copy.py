import sys

f = open(sys.argv[1], "r")
o = open(sys.argv[2], "w")
o.write(f.read())