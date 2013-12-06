f = open('0_2000.csv')
for line in f:
    fields = line.split(",")
    id = fields[0]
    tags = fields[1].strip()
    if (id != "Id"):
        print "%s,\"%s\"" % (id,tags)
    else:
        print line
