def runcursor(cursor, SQL):
	from datetime import datetime
	# print("runcursor")
	# print(SQL)
	cursor.execute(SQL)
	columns = [column[0] for column in cursor.description]
	results = []
	for row in cursor.fetchall():
		d = dict(zip(columns, row))
		for k,v in d.items():
			if type(v) == type(datetime(1970,1,1)):
				v = v.strftime("%Y-%m-%d")
			elif type(v) == type(None):
				val = "N/A"
			elif type(v) != type(""):
				v = str(v)
		results.append(d)
	return results
def getprojectinformation(cursor, UID, PWD, current = "current", log= []):
	try:
		current = current.replace("projects-","")
		try:
			lastQuery = sqlCall.objects.filter(callType="projects").latest()
			lastTimeStamp = lastQuery.timeStamp.strftime("%Y-%m-%dT%H:%M:%S")
			log.append(lastTimeStamp)
		except Exception as e:
			log.append(str(e))
			lastTimeStamp = "2019-10-01T05:05:00.000"
		
		if current == "current":
			SQL =			"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '%s' OR PR.ModDate >= '%s' AND PR.WBS2 = ' '" %(lastTimeStamp,lastTimeStamp)
			SQL_second =	"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '%s' OR PR.ModDate >= '%s' AND NOT PR.WBS2 = ' '" %(lastTimeStamp,lastTimeStamp)
		elif current == "all":
			SQL = 			"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '2015-01-01' AND PR.WBS2 = ' '"
			SQL_second =	"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '2015-01-01' AND NOT PR.WBS2 = ' '"
		elif current == "short":
			SQL =			"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '2019-01-01' AND PR.WBS2 = ' '"
			SQL_second =	"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.CreateDate >= '2019-01-01' AND NOT PR.WBS2 = ' '"
		elif "p-" in current:
			current = current.replace("p-","")
			SQL = 			"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '%s' AND PR.WBS2 = ' '"%(current)
			SQL_second = 	"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '%s' AND NOT PR.WBS2 = ' '"%(current)
			# SQL =			"SELECT * FROM PR WHERE WBS1 = '%s' AND WBS2 = ' '" %(current)
			# SQL_second =	"SELECT * FROM PR WHERE WBS1 = '%s' AND NOT WBS2 = ' '" %(current)
		else:
			# log.append(current)
			# log.append(current)
			SQL =			"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '%s' AND PR.WBS2 = ' '" %(current)
			SQL_second =	"SELECT * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '%s' AND NOT PR.WBS2 = ' '" %(current)

		qdict = runcursor(cursor, SQL)
		qdict += runcursor(cursor, SQL_second)
		# log.append(qdict)
		# proxyPhases = []
		# print("ran cursor")
		index = 0
		gdlen = len(qdict)

		return qdict
	except Exception as e:
		print(e)

def sqlcheck( UID, PWD, current = "current", log= []):
	try:
		import pyodbc
		cnxn = pyodbc.connect(DRIVER="SQL Server", SERVER="smartsydsql1.smartsoftwarecloud.com", DATABASE="Vision", UID=UID, PWD=PWD)
		cursor = cnxn.cursor()
		########## GET STAFF INFORMATION ##########
		qdict = getprojectinformation(cursor, UID, PWD, current = current, log = log)
		return qdict

	except Exception as e:
			print(e)


# q = sqlcheck("COXsqlreport","&hD$7R9k)j@G4(d", "p-218142.00")
q = sqlcheck("COXsqlreport","&hD$7R9k)j@G4(d", "all")
projfile = open("D:\\Users\\s-abutler\\Downloads\\projfile.tsv", "w")

import json
index = 1
for i in q:
	if i["WBS2"] == " ":
		i["TotalProjectCost"] = float(i["TotalProjectCost"])
		if i["TotalProjectCost"] > 0:
			if index == 1:
				index += 1
				with open("D:\\Users\\s-abutler\\Downloads\\proj.json", "w") as file_object:
					file_object.write(str(i))
			
			line = [i["WBS1"],i["Name"],i["TotalProjectCost"],i["custPrimarySector"],i["Address1"],i["Address2"],i["Address3"],i["City"],i["State"],i['Zip'],i['Country']]
			line = list(map(lambda x: str(x), line))
			nline = []
			for x in line:
				if x == "None" or x == None:
					x = ""
				nline.append(x)
			line = "\t".join(nline)+"\n"
			with open("D:\\Users\\s-abutler\\Downloads\\projfile.tsv", "a") as file_object:
				file_object.write(line)
			# if i["WBS1"] == '420060.00': print(i) 