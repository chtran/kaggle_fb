import csv
import json
import sys

def writefile(data, file_id):
    filename = 'test_'+str(file_id)+'.json'
    json_output = {}
    json_output["data"] = data
    newfile = open(filename, 'w')
    newfile.write(json.dumps(json_output))
    newfile.close()
    print "Wrote "+filename

filename = sys.argv[1]
csvfile = open(filename)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')

file_id = 0
data = []
N = 100000
for i,row in enumerate(reader):
    if i==0: continue
    if i%N == 0: 
        writefile(data, file_id)
        del data
        data = []
        file_id += 1
    item = {}
    item["id"] = int(row[0])
    item["title"] = row[1]
    item["text"] = row[2]
    data.append(item)

writefile(data, file_id)
print "Done processing "+str(i)+" questions"


