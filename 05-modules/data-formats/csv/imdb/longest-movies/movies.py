import json
import csv
import sys

if(len(sys.argv) > 1):
    csvfilepath = sys.argv[1]
    with open(csvfilepath) as file:
        csvdata = csv.DictReader(file)
        data = list(csvdata)
    

    sorted = data.sort(reverse=True)

    max = dict({'titel':'none','duur':0})   
    for item in data:
        if(int(item['duur'])>int(max['duur'])):
            max['titel']=item['titel']
            max['duur']=item['duur']
    print(max)
    #sorted = dict(sorted(data, key=lambda item: item[1]))
    print(data)
    print(sorted)