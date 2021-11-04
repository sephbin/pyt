import json
import requests


posturl = 'https://labs.cox.com.au/bd/rooms.json/?search=218018.00'
print("Send Get Request")
r = requests.get(posturl)
print("Recieved Get Request")
job = r.json()
check = ["data_text","data","Coordinates"]
headers = []
dataheaders = []
dataheaders_ = []
for r in job:
	for k in r:
		if k == "data":
			for nk in r[k]:
				if nk not in check:
					dataheaders.append(nk) 
					dataheaders_.append("|"+nk) 
		else:
			if k not in check: headers.append(k)

headers = list(set(headers))
dataheaders = list(set(dataheaders))
dataheaders_ = list(set(dataheaders_))

array = []
array.append("	".join(headers+dataheaders_))

for r in job:
	apob = []
	for k in headers:
		apob.append(str(r[k]))
	for k in dataheaders:
		try:
			apob.append(str(r["data"][k]))
		except:
			apob.append('')
	apob = "	".join(apob)
	array.append(apob)

array = "\n".join(array)
file = open("roomdata.tsv","w")
file.write(array)
file.close()