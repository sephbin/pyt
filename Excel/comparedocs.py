import xlrd
# import pandas as pd
# import numpy as np

def changeCH(ch, chNum):
	if chNum < 0:
		return "removed"
	elif chNum >= 2:
		return "locked"
	else:
		return ch

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
	sh = xlrd.open_workbook(loc).sheet_by_name(sheet_name)
	headers = []
	out = {}
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
			out[apob["element_id"]] = apob
	# print(out)
	return out

def cleanKey(k):
	k = k.replace("z_data.","").replace("SFS_","")
	return k

curV = getData('\\\\sydsrv01\projects\\2018\\218018.04\\06.0 SPECIFICATIONS & SCHEDULES\\6.2 Schedules\Doors\\SFS-COX-01-SH-AR91XX02-D.xlsx',sheet_name='Door Data')
oldV = getData('\\\\sydsrv01\projects\\2018\\218018.04\\06.0 SPECIFICATIONS & SCHEDULES\\6.2 Schedules\Doors\\SFS-COX-01-SH-AR91XX02-C.xlsx',sheet_name='Door Data')

# print(len(curV))
# print(len(oldV))
ignoreKeys = ["Combined Rooms", "z_data.Last Updated By", "Combined_EID", "EDIT LU", "CHECK NO", "CHEC NO 2", "CHECK NO 3", "CHEC MARK 2", "REMOVED MARK", "COMBINED", "B36", "Column1", "Column12", "Column2", "Column22", "Column23", "Column3", "Column5", "Column6", "COMBINED CONTAINMENT", "Combined Rooms", "room_combine", "CR-Check", "Mark Count", "mark_check", "mark_check_2", ]
change = False
chSet, ohSet = set(curV[list(curV)[0]]), set(oldV[list(oldV)[0]])

newKeys = list(chSet-ohSet)

out = [["ID", "Mark", "Key", "Prev", "New", "Action", "Hex", "CR-Check","Mark Count", "mark_check_2","mark_check","room_combine"]]
for c, cData in curV.items():
	mark = cData["mark"]
	chNum = int(cData["STATUS"])
	
	# print(c)
	if c in oldV:
		oData = oldV[c]
		# print("Exists", c)
		for cK, cV in cData.items():
			if cK in oData:
				ch = changeCH("changed", chNum)
				if cK in ignoreKeys:
					continue
				oV = oData[cK]
				try:
					cV = float(cV)
					oV = float(oV)
				except:
					pass
				if cV == 0.0 or cV == "":
					cV = None
				if oV == 0.0 or oV == "":
					oV = None
				if cV != oV:
					if not cV:
						cV = "-empty-"
					if not oV:
						oV = "-empty-"
					out.append([c, mark, cleanKey(cK), oV, cV, ch])
					change = True
			else:
				# print(cK)
				pass
		for nK in newKeys:
			ch = changeCH("added", chNum)
			if nK in ignoreKeys:
				continue
			nV = cData[nK]
			if nV == 0.0 or nV == "":
				nV = None
			if nV:
				if not nV:
					nV = "-empty-"
				out.append([c, mark, cleanKey(nK), "", nV, ch])
	else:
		print("c not in oldV")
		for cK, cV in cData.items():
			ch = changeCH("new", chNum)
			if cK in ignoreKeys:
				continue
			oV = None
			try:
				cV = float(cV)
				oV = float(oV)
			except:
				pass
			if cV == 0.0 or cV == "":
				cV = None
			if oV == 0.0 or oV == "":
				oV = None
			if cV != oV:
				if not cV:
					cV = "-empty-"
				if not oV:
					oV = "-empty-"
				out.append([c, mark, cleanKey(cK), oV, cV, ch])
				change = True
		pass
	# if change:
	# 	break

for c, cData in oldV.items():
	mark = cData["mark"]
	if c not in curV:
		# print("Exists", c)
		for cK, cV in cData.items():
			if cK not in ignoreKeys:
				try:
					oV = float(0)
					cV = float(cV)
				except:
					pass
				if cV == 0.0 or cV == "":
					cV = None
				if oV == 0.0 or oV == "":
					oV = None
				if cV != oV:
					if not cV:
						cV = "-empty-"
					if not oV:
						oV = "-empty-"
					out.append([c, mark, cleanKey(cK), oV, cV, "removed"])
					change = True
	else:
		# print(cK)
		pass
print(out[:5])
nout = []
for o in out:
	o = list(map(lambda x: str(x), o))
	o = "\t".join(o)
	nout.append(o)
nout = "\n".join(nout)

with open("D:\\Users\\s-abutler\\Downloads\\compare_C-D.tsv", "w") as f:
	f.write(nout)
	print("written")