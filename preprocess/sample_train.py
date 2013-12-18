import csv
import json
import sys
import random

filename = sys.argv[1]
N = int(sys.argv[2])
output_file = sys.argv[3]

csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
new_csv = open(output_file, 'w')
writer = csv.writer(new_csv, delimiter=',', quotechar='"')

data = []
for i,row in enumerate(reader):
    if (i==N): break
    writer.writerow(row)
