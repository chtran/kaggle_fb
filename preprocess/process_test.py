import csv
import json
import sys

filename = sys.argv[1]
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')

data = []
N = 1000
for i,row in enumerate(reader):
    if i==0: continue
    if i>N: break
    item = {}
    item["id"] = int(row[0])
    item["title"] = row[1]
    item["text"] = row[2]
    data.append(item)

json_output = {}
json_output["data"] = data
print json.dumps(json_output)
