import csv
import json

### Need to manipulate json data before writing to csv



infile = open('AllCards.json','r')
outfile = open('csvCardList.csv','w')

writer = csv.writer(outfile)

for row in json.loads(infile.read()):
    writer.writerow(row)