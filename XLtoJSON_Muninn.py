import xlrd
import json

import requests
import urllib
import re
import os

from datetime import date

##################################################################

# POSTURL SETUP

pro_num = '218018.00'

url_start = "https://labs.cox.com.au/"


model = "doors"
upper_model_lut = {}
url_lut = {
	"doors": "bd/capi/doors/",
}

posturl = url_start + url_lut[model]

# FILE LOCATION

# directory = "C:\\Users\\Emily\\Documents\\01_Files\\04_Cox\\3_Remote\\Excel"
# filename = "FF&E_Schedule_-_Room_Casework.xlsx"

today = date.today()

directory = "\\\\sydsrv01\\projects\\2018\\218018.04\\06.0 SPECIFICATIONS & SCHEDULES\\6.2 Schedules\\Doors"
# directory = input("Enter directory path: ")

filepath = directory

# filename = input("Enter filename: ")
filename = "Door Schedule - Working.xlsx"

file = os.path.join(filepath, filename)

##################################################################

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(1)

out = []

topost = {}
topost["data"] = []

# for k,v in zip(sheet.row_values(0), sheet.row_values(1)):
# 	print(k, type(v))

test = []

for i in range(sheet.nrows):

	# Creating TSV
	
	row = []

	# for k,v in zip(sheet.row_values(0), sheet.row_values(i)):

	# 	if re.search(r"^\W+$", k) == None:
	# 		row.append(str(v))

	# test.append(row)

	# Creating Dictionaries

	if i != 0:
		
		obj = {}
		obj["data"] = {}
		data_obj = {}
		
		for k,v in zip(sheet.row_values(0), sheet.row_values(i)):
			if re.search(r"^\W+$", k) == None:

				key = k

				try:
					x = upper_model_lut[model]["other_base"]
					if key in x:
						if v == "(none)":
							obj[key] = ""
						else:
							obj[key] = v
					else:
						data_obj[key] = str(v)
						obj["data"] = data_obj
				except:

					if key == "Room":
						if type(v) != type("string"):
							val = int(v)
						else:
							val = v

						if val == "":
							val = "XXXXXXXX"
						data_obj[key] = pro_num + "|" + str(val)
					else:
						data_obj[key] = str(v)
						obj["data"] = data_obj

		try:
			test_1 = obj["data"]["source_file_1"]
			test_2 = obj["data"]["source_file_2"]

			if test_2 == "":
				try:
					# source_file = test_1.split(".")[0] + ".rvt"
					if test_1 == "COX-SFS-ARCHITECTURE-R19.rvt":
						source_file = base_source_file
					else:
						source_file = test_1.split(".")[0] + ".rvt"
				except:
					source_file = test_1 + ".rvt"
			else:

				try:
					source_file = test_2.split(".")[0] + ".rvt"
				except:
					source_file = test_2 + ".rvt"

		except Exception as e:
			if obj["data"]["source_file_1"] == "":
				source_file = base_source_file
			else:
				source_file = obj["data"]["source_file_1"]

		try:
			y = upper_model_lut[model]["other_base"]
			if "source_file" in y:
				obj["source_file"] = source_file
			else:
				obj["data"]["source_file"] = source_file
		except:
			obj["data"]["source_file"] = source_file

		try:
			del obj["data"]["source_file_1"]
			del obj["data"]["source_file_2"]
		except:
			pass

		out.append(obj)

def createTSV(test, file):
	test = list(map(lambda x: "\t".join(x), test))
	test = "\n".join(test)
	pre, ext = os.path.splitext(file)
	file = open(pre + ".tsv","w")
	file.write(test)
	file.close()
	print("DONE")

# createTSV(test, file)

def createJSON(out, file):
	pre, ext = os.path.splitext(file)
	file = open(pre + ".json","w")
	file.write(json.dumps(out, indent=4))
	file.close()

createJSON(out, file)
# print(out[3])
# print(out[4])

topost["data"] = json.dumps(out)
topost["bulktype"] = "deleteunused"

def postme(posturl, topost):
	try:
		r = requests.post(posturl, topost)
		job = r.json()
		print(job)
	except Exception as e:
		print(e)

# postme(posturl, topost)