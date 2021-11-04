import csv
with open('doorsfuckthis.tsv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
	headers = ['Hardware Set','Sign Panel Type','Kickplate','Hinge Type','Seal Type','Door Closer','Door Stop','Keying','Security','Vision Panel']
	for row in spamreader:
		text = []
		for header, item in zip (headers,row):
			if item != "":
				text.append(header+": "+item)
		text = "; ".join(text)
		print(text)