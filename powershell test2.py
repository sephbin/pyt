
import subprocess
import sys
import re
import requests
import json
from fuzzywuzzy import fuzz, process

p = subprocess.check_output(['powershell.exe', 'Get-ADComputer -Filter \'Enabled -eq "True"\' -Properties Description | FT Name,Description'], shell=True).decode("utf-8", errors="ignore")
p = p.split("\r\n")


clist = []
for i, r in enumerate(p):
	# if "677" in r.lower():
	if i > 2:
		vre = re.sub(r"  +",r"\t",r)
		vre = re.sub(r" {",r"\t{",vre)
		vre = re.sub(r"True ",r"True\t",vre)
		vre = re.sub(r"False ",r"False\t",vre)
		# print(vre)
		r = vre.split("\t")
		out = []
		# print("----",r)
		# print(vre)
		# for v in r:
			# if v != "":
				# out.append(v)
				# print(v)
		try:	clist.append(r)
		except:	pass
		# print("----",out)
clist.sort()
# print(clist)
ci = 0

# print(clist)

staff = requests.get("http://workshop.cox.com.au/oj/api/staff_details.json/").json()
staffNames = list(map(lambda x: x["name"].lower(), staff))
# print(staffNames[0])
change = []
for cn in clist:
	if "SYD" in cn[0] or "COX-RD" in cn[0]:
		l = cn[1].lower()
		m = l.split(" - ")[0]
		# print(">",m, cn)
		staffid = None
		if m != " " and m != "" and " " in m:
			f = process.extract(m,staffNames)
			# print(f)
			f = f[0]
			if f[1] > 85:
				staff_index = staffNames.index(f[0])
				staffid = staff[staff_index]["id"]
			# print(f, staffid)
# 			rg = requests.get("http://workshop.cox.com.au/oj/api/staff_details.json/?search=%s"%(m))
# 			try:
# 				staffid = rg.json()[0]['id']
# 			except Exception as e: print(e)
		change.append({"obtype":"hardware","key":"staff","value":staffid,"pk":"number","pv":cn[0]})
url = 'http://workshop.cox.com.au/oj/functions/edit/'
myobj = {'data': change}
# print(myobj)
x = requests.post(url, data = json.dumps(myobj))
print("user update",json.dumps(x.json()))

print(clist)
cnlist = list(map(lambda x: x[0], clist))


rg = requests.get("http://workshop.cox.com.au/oj/api/hardwares.json/")
change = []
for h in rg.json():
	if h["elementType"] == 2:
		if h["number"] not in cnlist:
			# print(h["number"])
			change.append({"obtype":"hardware","key":"enabled","value":False,"pk":"number","pv":h["number"]})
url = 'http://workshop.cox.com.au/oj/functions/edit/'
myobj = {'data': change}
# print(myobj)
x = requests.post(url, data = json.dumps(myobj))
print("decom", json.dumps(x.json()))

missingUser = []
for h in rg.json():
	print(h)
	if h["elementType"] == 2:
		if "-" in h["number"]:
			if not h["staff"]:
				missingUser.append(h["number"])

for c in missingUser:
	try:
		p = subprocess.check_output(['powershell.exe', r'ping -n 1 %s'%(c)], shell=True).decode("utf-8", errors="ignore")
		if "unreachable" not in p:
			p = subprocess.check_output(['powershell.exe', r'C:\PSTools\PsLoggedOn \\%s'%(c)], shell=True).decode("utf-8", errors="ignore")
			p = p.split("\r\n")
			for l in p:
				if "COXGROUP" in l:
					print(c, l)
	except:
		print(c,"ping failed")
		pass
