from statistics import mean
import sys
import json
from datetime import datetime

with open('input.txt') as file:
    data = [ (datetime.strptime(date, '%d/%m/%Y'), temps) for date, temps in json.load(file).items() ]

with open("output.txt","w") as output:
    for _, temps in sorted(data, key=lambda p: p[0]):
        output.write(f'{round(mean(temps))}\n')

# print(data)