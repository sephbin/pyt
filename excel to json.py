from time import sleep
import xlrd
# import pandas as pd
# import numpy as np

def getDataNumOnly(loc="", sheet_name=None):
	data =  pd.read_excel(loc, sheet_name).to_dict()
	# print(read(pd))
	# print(dir(data))

	out = {}
	listData = {}
	for k,v in data.items():
		# print(k)
		for i, o in v.items():
			# print(k, i, o)
			if str(i) not in out:
				out[str(i)] = {}
			out[str(i)][k] = o
			# print(out)
			# break
		# break	
	# print(len(out))
	# print(out["2"])
	for r in range(len(out)):
		listData[out[str(r)]["element_id"]] = out[str(r)]
	return listData

def getData(loc="", sheet_name=None):
	sh = xlrd.open_workbook(loc)
	if sheet_name:
		sh = sh.sheet_by_name(sheet_name)
	else:
		sh = sh.sheet_by_index(0)
	headers = []
	out = []
	for rx in range(sh.nrows):
		row = sh.row(rx)
		apob = {}
		for rv, v in enumerate(row):
			if rx == 0:
				headers.append(v.value)
			else:
				val = v.value
				if headers[rv] == "element_id":
					val = str(int(val))
				apob[headers[rv]] = val
		if rx != 0:
			out.append(apob)
	# print(out)
	return out

def cleanKey(k):
	k = k.replace("z_data.","").replace("SFS_","")
	return k
curV = getData('D:\\Users\\s-abutler\\Downloads\\Drawing Register - Migrate.xlsx'
# ,sheet_name='Door Data'
)
import json
import requests

print(json.dumps(curV[0]))
# for  i, c in enumerate(curV):
# 	print(i,c["Drawing Title"])

for c in curV:
	c["project"] = "218018.11"
	c["name"] = c["Drawing Title"]
	c["identifier"] = c["Drawing Number"]
	c["elementModel"] = "document"

payload = {"clear": False, "elements":curV}

r = requests.post("http://labs.cox.com.au/muninn_dev/CRUD/", data=json.dumps(payload))
print(r.json())