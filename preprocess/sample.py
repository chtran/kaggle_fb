import csv
import json
import sys
import random

filename = sys.argv[1]
percent = float(sys.argv[2])
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')

data = []
for i,row in enumerate(reader):
    if i==0: continue
    if (random.uniform(0,100) > percent): continue
    item = {}
    item["id"] = int(row[0])
    item["title"] = row[1]
    item["text"] = row[2]
    item["tags"] = row[3].split()
    data.append(item)

json_output = {}
json_output["data"] = data
print json.dumps(json_output)
