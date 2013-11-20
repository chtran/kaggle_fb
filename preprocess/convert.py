import csv
import json
import sys
import random

filename = sys.argv[1]
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')

data = []
header = True
for row in reader:
    if (header):
        header = False
        continue
    item = {}
    item["id"] = int(row[0])
    item["title"] = row[1]
    item["text"] = row[2]
    item["tags"] = row[3].split()
    data.append(item)

json_output = {}
json_output["data"] = data
print json.dumps(json_output)
