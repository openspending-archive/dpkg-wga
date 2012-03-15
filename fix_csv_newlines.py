import csv, sys

infile = sys.argv[1]
outfile = sys.argv[2]

fho = open(outfile, 'wb')
reader = csv.reader(open(infile, 'rbU'), delimiter='|', lineterminator='\r\n')
writer = csv.writer(fho, quotechar='"')
overlap = []
for i, row in enumerate(reader):
    if len(row)<7:
	overlap.extend(row)
	continue
    elif len(overlap):
	overlap[-1] = overlap[-1] + '\n' + row[0]
        row = overlap + row[1:]
        overlap = []
    writer.writerow(row)

fho.close()
