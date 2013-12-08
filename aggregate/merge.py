import csv
dic={}
n=20
for i in range(n):
    filename = "data/"+str(i*100)+"_"+str(i*100+100)+".csv"
    csv_file = open(filename)
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        id = row[0]
        tags = row[1]
        if id not in dic:
            dic[id] = ""
        if len(tags)>0 and len(dic[id])>0:
            dic[id] += " "
        dic[id] += tags


output_name = "0_"+str(n*100)+".csv"
csv_file = open(output_name, 'w')
writer = csv.writer(csv_file, quotechar='"', delimiter=',')
for id in sorted(dic.keys()):
    writer.writerow([id, dic[id]])


