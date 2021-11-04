import csv
import json
import requests
rlist = []

log = []

rlistarray = []
postdata = []
def run_2():
	with open("ASD.tsv") as tsvfile:
		reader = csv.DictReader(tsvfile, delimiter='\t')
		for row in reader:
			outdict = {"data":{}}
			for k,v in row.items():
				print(k,v)
				if k == "id":
					outdict[k]=v
				else:
					outdict["data"][k]=v

			postdata.append(dict(outdict))

run_2()

# print(postdata)
# postdata = [postdata[0]]

url = 'https://labs.cox.com.au/muninn_dev/capi/room_type/update_or_create/'
myobj = {'data': json.dumps(postdata), 'project__number': '219180.00'}

x = requests.post(url, data = myobj)
print(x.text)