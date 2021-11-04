import json
from sys import breakpointhook
import requests
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
		apob = {"isIssued":True}
		listItems = []
		for rv, v in enumerate(row):
			if rx == 0:
				headers.append(v.value)
			else:
				val = v.value
				if headers[rv] == "element_id":
					val = str(int(val))
				if headers[rv] == "issueDate":
					val = str(val)
					val = "20"+val[0]+val[1]+"-"+val[2]+val[3]+"-"+val[4]+val[5]
				if "SFS-" in headers[rv]:
					if val != "":
						listItems.append(headers[rv])
				else:
					apob[headers[rv]] = val
		# listItems = list(map(lambda x: "^"+x+"$", listItems))
		if rx != 0:
			query = "|".join(listItems)
			# print("q",query)
			url = "http://labs.cox.com.au/muninn_dev/documents.json/?search="+query
			# print("u",url)
			docrequest = requests.get(url)
			try:
				drjson = docrequest.json()
			except:
				print(docrequest.text)
			# print(drjson)
			idlist = []
			if drjson == []:
				continue
			for dr in drjson:
				print(dr["id"],dr["identifier"])
				# print(dr["id"])
				idlist.append({"id":dr["id"]})
			# apob["documentsIssued"] = idlist
			apob["_add_documentsToIssue"] = idlist
			apob["_add_documentsIssued"] = idlist
			out.append(apob)
			# break
	# print(out)
	return out

def cleanKey(k):
	k = k.replace("z_data.","").replace("SFS_","")
	return k
curV = getData('D:\\Users\\s-abutler\\Downloads\\Drawing Register - Migrate (1).xlsx'
# ,sheet_name='Door Data'
)

# print(json.dumps(curV[0]))
# print(json.dumps(curV[100]))
# curV = curV[:1]
# print(curV)
# for  i, c in enumerate(curV):
# 	print(i,c["Drawing Title"])

for c in curV:
	c["project"] = "218018.11"
# 	c["name"] = c["Drawing Title"]
# 	c["identifier"] = c["Drawing Number"]
	c["elementModel"] = "issue"

payload = {"clear": False, "elements":curV}
print(payload)
r = requests.post("http://labs.cox.com.au/muninn_dev/CRUD/", data=json.dumps(payload))
# r = requests.post("http://localHost:8000/muninn_dev/CRUD/", data=json.dumps(payload))
print(r.json())