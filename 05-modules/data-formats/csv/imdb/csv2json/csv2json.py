import json
import csv
import sys

if(len(sys.argv) > 1):
    csvfilepath = sys.argv[1]
    with open(csvfilepath) as file:
        csvdata = csv.DictReader(file)
        data = list(csvdata)
    with open('example.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))
    

print(data)