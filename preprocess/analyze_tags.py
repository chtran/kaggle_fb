import csv
import json
import sys
import random

csv_file = open(sys.argv[1])
reader = csv.reader(csv_file, delimiter=',', quotechar='"')

tag_file = open(sys.argv[2])
sorted_tags = json.load(tag_file)

N = int(sys.argv[3])
tags = set(map(lambda x: x[0], sorted_tags[:N]))
data = []
header = True
found = 0.
for row in reader:
    if (header):
        header = False
        continue
    q_tags = row[3].split()
    for q_tag in q_tags:
        if q_tag in tags:
            found += 1
            break

print "Questions with tag found: ",found
