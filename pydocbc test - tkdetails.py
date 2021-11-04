import pyodbc
import json
import datetime
# Specifying the ODBC driver, server name, database, etc. directly
# cnxn = pyodbc.connect(DRIVER="SQL Server", SERVER="smartsydsql1.smartsoftwarecloud.com", DATABASE="Vision", UID="COXsqlreport", PWD="&hD$7R9k)j@G4(d",)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=20.191.192.100;DATABASE=VP;UID=COXsqlreport;PWD=&hD$7R9k)j@G4(d')

def runcursor(cursor, SQL):
	cursor.execute(SQL)
	columns = [column[0] for column in cursor.description]
	results = []
	# print(cursor, dir(cursor))
	# print(cursor.tables())
	# for row in cursor.statistics("tkDetail"):
		# print(row)
		
	for row in cursor.fetchall():
		results.append(dict(zip(columns, row)))
	return results
# Create a cursor from the connection
cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
# cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
SQL = [
# "SELECT * FROM INFORMATION_SCHEMA.TABLES",
# "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'ClientAlias'",
# "SELECT Name, LongName, WBS1, WBS2, WBS3 FROM PR WHERE WBS1='220148.00'"
# "SELECT * FROM PR WHERE WBS1='219014.01'"
# "SELECT * FROM PR WHERE WBS1='214083.00'"
# '''
# SELECT *
#  FROM ProjectCustomTabFields c
#  JOIN PR
#  ON c.WBS1 = PR.WBS1
#  WHERE c.custProjectSheet = 'Y'
#  AND PR.WBS2 = ''
# '''
# "SELECT TOP 1 * FROM PR WHERE ModDate >= '2019-10-01'"
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'EM'",
# "SELECT * FROM EM WHERE ModDate >= '2019-10-01'",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'EmployeeCustomTabFields'",
# "SELECT * FROM EmployeeCustomTabFields",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'LD'",
# AND WBS1='218018.04'
# "SELECT TOP 1 * FROM LD  WHERE PKey > '631896745239' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey DESC",
# "SELECT TOP 1 * FROM LD WHERE WBS1='000010.00' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey DESC",
# "SELECT * FROM LD WHERE WBS1 LIKE '%217102.00%' AND WBS2 = '043' AND PKey NOT LIKE '%[A-Z]%' AND TransType='LA' ORDER BY PKey DESC",
# "SELECT * FROM LD WHERE WBS1 LIKE '%217102%' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey ASC",
# "SELECT TOP 1 * FROM EM ORDER BY ModDate DESC",
# "SELECT TOP 1 * FROM EM WHERE Employee = '3059'",
	# "SELECT TOP 50 * FROM LedgerEX WHERE WBS1='217102.03'",
	"SELECT TOP 50 * FROM LedgerAR WHERE WBS1 LIKE '217102.%' AND Account LIKE '4%' ORDER BY TransDate DESC",
	# "SELECT TOP 50 * FROM LedgerMisc WHERE WBS1='217102.03'",
	# "SELECT TOP 50 * FROM LedgerAP WHERE WBS1='217102.03'",
	# "SELECT TOP 50 * FROM BT WHERE WBS1 LIKE '217102.%'",
# "SELECT TOP 1 * FROM LedgerMisc	 WHERE Desc1 LIKE 'Virtunet%' ORDER BY TransDate DESC",
# "SELECT TOP 1 * FROM LedgerAR	 WHERE Desc1 LIKE 'Virtunet%' ORDER BY TransDate DESC",
# "SELECT TOP 1 * FROM LedgerEX	 WHERE Desc1 LIKE 'Virtunet%' ORDER BY TransDate DESC",
# "SELECT TOP 1000 * FROM LedgerAP	 WHERE Desc1 LIKE 'Virtunet%' ORDER BY TransDate DESC",
# "SELECT TOP 1 * FROM LedgerAR WHERE Desc1 LIKE '%irtu%'",
# "SELECT TOP 1 * FROM LedgerEX WHERE Desc1 LIKE '%%irtu%%'",
# "SELECT TOP 10 * FROM LedgerAP WHERE (CAST(Period AS BIGINT)*100000) + CAST(PostSeq AS BIGINT) > 20210400000 ORDER BY TransDate ASC",
# "SELECT TOP 1 * FROM EMMain",
# "SELECT TOP 1 * FROM EMDegree",
# "SELECT TOP 4 * FROM tkDetail ORDER BY TransDate DESC" ,
# TOP 1 *
# '''SELECT 	
# *
# FROM tkMaster m
# JOIN tkDetail d
#   ON d.Employee = m.Employee
#   AND d.EndDate = m.EndDate
# JOIN PR p
#   ON d.WBS1 = p.WBS1
# JOIN ProjectCustomTabFields c
#   ON d.WBS1 = c.WBS1
# WHERE m.CreateUser = 'S-ELEUNG'
# ORDER BY m.ModDate ASC

# ''' ,
# ORDER BY d.WBS1 ASC
# AND m.ModDate >= '2020-10-03T05:05:00.000'
# "SELECT TOP 20 * FROM BTRCT ORDER BY TableNo DESC",
# "SELECT TOP 10 * FROM LD WHERE PKey > '550000000000' AND PrOrg LIKE '%SYD%' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey",
# "SELECT TOP 10 * FROM LD WHERE PKey > '550000000000' AND PrOrg LIKE '%SYD%' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'ProjectCustomTabFields'",
# "SELECT TOP 50 * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '218018.09' ORDER BY PR.ModDate",
# "SELECT * FROM CL WHERE ClientID='E9A8650AF9494AFFAAD6EF8369F58ED0'",
# "SELECT TOP 50 * FROM LedgerAP",
# "SELECT TOP 50 * FROM LedgerAP",
	# "SELECT TOP 1 * FROM BT",	#Billing Terms Table
	# "SELECT TOP 1 * FROM BTLaborCatsData",	#Billing Configuration Table - Labor Categories
	# "SELECT TOP 1 * FROM BTLaborCatsDescriptions",	#Billing Configuration Table - Labor Category Descriptions, by Language
	# "SELECT TOP 1 * FROM BTRCT",	#Billing Rate Table - Labor Category Tables
	# "SELECT TOP 1 * FROM BTRCTCats",	#Billing Rate Table - Labor Categories
	# "SELECT TOP 1 * FROM CFGEmployeeTitle",	#
	# "SELECT TOP 1 * FROM CFGEmployeeType",	#
	# "SELECT TOP 1 * FROM CL",	#
	# "SELECT TOP 1 * FROM dtproperties",	#Empty
	# "SELECT TOP 1 * FROM EM",	#
	# "SELECT TOP 1 * FROM EMDegree",	#
	# "SELECT TOP 1 * FROM EmployeeCustomTabFields",	#
	# "SELECT TOP 1 * FROM EMSkills",	#
	# "SELECT TOP 1 * FROM LD",	#
	# "SELECT TOP 1 * FROM LedgerAP",	#Expense Detail Table - Accounts Payable
	# "SELECT TOP 1 * FROM LedgerAR",	#Expense Detail Table - Accounts Receivable
	# "SELECT TOP 1 * FROM LedgerEX",	#Expense Detail Table
	# "SELECT TOP 1 * FROM LedgerMisc",	#Expense Detail Table - Miscellaneous Expense
	# "SELECT TOP 1 * FROM PR",	#
	# "SELECT TOP 1 * FROM ProjectCustomTabFields",	#
	# "SELECT TOP 1 * FROM tkComments",	#
	# "SELECT TOP 1 * FROM tkControl",	#
	# "SELECT TOP 1 * FROM tkCustomFields",	#
	# "SELECT TOP 1 * FROM tkDetail",	#
	# "SELECT TOP 1 * FROM tkMaster",	#
	# "SELECT TOP 1 * FROM tkRevExplanations",	#
	# "SELECT TOP 1 * FROM tkRevisionDetail",	#
	# "SELECT TOP 1 * FROM tkRevisionMaster",	#
	# "SELECT TOP 1 * FROM tkUnitDetail",	#
]

chHeaders = [
"TABLE_NAME",
# "COLUMN_NAME",
]

prHeaders = [
"Status",
"WBS1",
"WBS2",
"WBS3",
"CreateDate",
"StartDate",
"Name",
# "LongName",
"Principal",
"ProjMgr",
"Supervisor",
]

stHeaders = [
"Status",
"Employee",
"Location",
"State",
"PreferredName",
"FirstName",
"MiddleName",
"LastName",
"EMail",
"Title",
"WorkPhone",
"WorkPhoneExt",
"MobilePhone",
# "CreateDate",
# "ModDate",

]

stCustHeaders = [
"Employee",
"CreateUser",
"CreateDate",
"ModDate",
"ModUser",
]

ldCustHeaders = [
"EmOrg",
"PrOrg",
"PKey",
"WBS1",
"WBS2",
"WBS3",
"Employee",
"Name",
"Period",
"RegHrs",
"OvtHrs",
"Rate",
"RegAmt",
"OvtAmt",
"ProjectCost",
"BilledPeriod",
"TransDate",
]
pctfCustHeaders = [
"WBS1",
"WBS2",
"WBS3",
"Principal",
"custPrimarySector",
]

setList = {}
# headers = pctfCustHeaders
headers = chHeaders
print("-------")
total = 0
for i in SQL:
	print("-------")
	print(i)
	# print("\t".join(headers))
	try:
		out = []
		qdict = runcursor(cursor, i)
		# print(qdict)
		for ind, q in enumerate(qdict):
			# print("----------------------------")
			table = []
			# print(ind,q)
			# try:	print(q["TABLE_NAME"])
			# except:	pass
			# total += float(q["RegAmt"])
			# print(q["PostSeq"],total,q["RegAmt"],q["Name"],q["WBS1"],q["WBS2"],q["WBS3"])
			# apob = [q["WBS1"], q["LongName"], q["custPrimarySector"],q["Address1"],q["Address2"],q["Address3"],q["City"],q["State"],q["Zip"],q["Country"]]
			# apob = "\t".join(list(map(lambda x: str(x), apob)))
			# with open(r"D:\Users\s-abutler\Downloads\projects.tsv", "a") as f:
				# f.write(apob+"\n")
			# print(q["WBS1"])
			# setList.append(q["WBS1"])
			# if q["WBS1"] not in setList:
			# 	apob = {"number":q["WBS1"], "name": q["LongName"], "hrs":0 , "sector": q["custPrimarySector"]}
			# else:
			# 	apob = setList[q["WBS1"]]
			# apob["date"] = q["ModDate"].strftime("%Y%m%d")
			# apob["hrs"] += float(q["RegHrs"])+float(q["OvtHrs"])
			# setList[q["WBS1"]] = apob
			print("\t".join(["",str(q['TransDate']),q['Desc1'],q['Desc2'],str(q['Account']),str(q['Amount'])]))
			for k, v in q.items():
				# if "FeeFactor1" in k or "WBS1" in k or "WBS2" in k:
				# print("	"+str(k)+"	"+str(v))
				pass
			# print("-------")
			# for h in headers:
			# 	val = q[h]``
			# 	if type(val) == type(datetime.datetime(1970,1,1)):
			# 		val = val.strftime("%Y-%m-%d")
			# 	elif type(val) == type(None):
			# 		val = "N/A"
			# 	elif type(val) != type(""):
			# 		val = str(val)
			# 	table.append(val)
			# print("\t".join(table))
	except Exception as e:
		print(e)
		# print(qdict)

# for i in setList:
# 	print(i)
print(setList)

# headers = list(setList[list(setList)[0]])
# for k,v in setList.items():
# 	txt = ""
# 	print(v)
# 	for h in headers:
# 		txt += str(v[h])+"\t"
# 	print(txt)