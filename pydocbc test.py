import pyodbc
import json
import datetime
# Specifying the ODBC driver, server name, database, etc. directly
# cnxn = pyodbc.connect(DRIVER="SQL Server", SERVER="smartsydsql1.smartsoftwarecloud.com", DATABASE="Vision", UID="COXsqlreport", PWD="&hD$7R9k)j@G4(d",)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=smartsydsql1.smartsoftwarecloud.com;DATABASE=VP;UID=COXsqlreport;PWD=&hD$7R9k)j@G4(d')

def runcursor(cursor, SQL):
	cursor.execute(SQL)
	columns = [column[0] for column in cursor.description]
	results = []
	print(cursor, dir(cursor))
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
# "SELECT * FROM PR WHERE WBS1='218018.04'"
# "SELECT * FROM PR WHERE ModDate >= '2019-10-01'"
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'EM'",
# "SELECT * FROM EM WHERE ModDate >= '2019-10-01'",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'EmployeeCustomTabFields'",
# "SELECT * FROM EmployeeCustomTabFields",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'LD'",
# AND WBS1='218018.04'
# "SELECT TOP 1 * FROM LD  WHERE PKey > '631896745239' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey DESC",
# "SELECT TOP 1 * FROM EM",
# "SELECT TOP 1 * FROM EMDegree",
# "SELECT TOP 4 * FROM tkDetail ORDER BY TransDate DESC" ,
"SELECT TOP 4 * FROM tkMaster ORDER BY ModDate DESC" ,
# "SELECT TOP 20 * FROM BTRCT ORDER BY TableNo DESC",
# "SELECT TOP 10 * FROM LD WHERE PKey > '550000000000' AND PrOrg LIKE '%SYD%' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey",
# "SELECT TOP 10 * FROM LD WHERE PKey > '550000000000' AND PrOrg LIKE '%SYD%' AND PKey NOT LIKE '%[A-Z]%' ORDER BY PKey",
# "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'ProjectCustomTabFields'",
# "SELECT TOP 50 * FROM PR INNER JOIN ProjectCustomTabFields ON PR.WBS1=ProjectCustomTabFields.WBS1 AND PR.WBS2=ProjectCustomTabFields.WBS2 AND PR.WBS3=ProjectCustomTabFields.WBS3 WHERE PR.WBS1 = '218018.09' ORDER BY PR.ModDate",
# "SELECT * FROM CL WHERE ClientID='E9A8650AF9494AFFAAD6EF8369F58ED0'",
# "SELECT TOP 50 * FROM LedgerAP",
# "SELECT TOP 50 * FROM LedgerAP",
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

# headers = pctfCustHeaders
headers = chHeaders
for i in SQL:
	
	# print("\t".join(headers))
	try:
		qdict = runcursor(cursor, i)
		# print(qdict)
		for q in qdict:
			print("----------------------------")
			table = []
			# print(q)
			for k, v in q.items():
				print(k,": ", v)
				pass
			# for h in headers:
			# 	val = q[h]
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