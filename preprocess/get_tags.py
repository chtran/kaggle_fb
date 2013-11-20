import csv
import json
import sys

filename = sys.argv[1]
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')

tag_count = {}
for row in reader:
    tags = row[3].split()
    for tag in tags:
        if tag in tag_count:
            tag_count[tag] += 1
        else:
            tag_count[tag] = 1

print json.dumps(tag_count)
