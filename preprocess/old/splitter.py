import csv
import json
import sys

filename = sys.argv[1]
N = int(sys.argv[2])
offset = int(sys.argv[3])
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
i = -1
t = 0

data = []
for row in reader:
    i += 1
    if (i<offset): continue
    if (i==0): continue
    if (t == N): break
    t +=1
    item = {}
    item["id"] = int(row[0])
    item["title"] = row[1]
    item["text"] = row[2]
    item["tags"] = row[3].split()
    data.append(item)

json_output = {}
json_output["data"] = data
print json.dumps(json_output)
