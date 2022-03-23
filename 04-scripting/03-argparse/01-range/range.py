import argparse

parser = argparse.ArgumentParser(prog='range')
parser.add_argument('start', type=int)
parser.add_argument('end', type=int)
parser.add_argument('-x', '--exclusive', action='store_true')
parser.add_argument('--step', type=int, default=1)

# Parses sys.argv and stores parameters in args
args = parser.parse_args()

print(args)

for i in range(args.start,(args.end if args.exclusive else args.end+1),args.step):
    print(i)

#if(args.exclusive):
#    for i in range(args.start,args.end,args.step):
#        print(i)
#else:
#    for i in range(args.start,args.end+1,args.step):
#        print(i)