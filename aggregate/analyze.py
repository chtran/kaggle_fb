import csv
f = open('quoted.csv')
reader = csv.reader(f)
q = 0.
t = 0.
no = 0.

for row in reader:
    q += 1
    t += len(row[1].split())
    if len(row[1].split())==0:
        no += 1
print "Number of quesitons: ",q
print "Number of tags predicted: ",t
print "Number of question without tags: ",no
print "Tag per question: ",t/q

