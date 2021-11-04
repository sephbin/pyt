import subprocess
import sys
import re
import requests
import json

p = subprocess.check_output(['powershell.exe', 'Get-ADComputer -Filter * | FT *'], shell=True).decode("utf-8")
p = p.split("\r\n")

clist = []
for i, r in enumerate(p):
	if i > 2:
		vre = re.sub(r"  +",r"\t",r)
		vre = re.sub(r"} {",r"}\t{",vre)
		# print(vre)
		r = vre.split("\t")
		out = []
		# print("----",r)
		# print(vre)
		for v in r:
			if v != "":
				out.append(v)
				# print(v)
		try:	clist.append(out[1].split(".")[0].replace("True ",""))
		except:	pass
		# print("----",out)
clist.sort()
print(clist)
ci = 0
for cn in clist[::-1]:
	if "SYD-WS" in cn or "COX-RD" in cn:
	# if "SYD-WS-686" in cn:
		# p = subprocess.Popen(['powershell.exe', 'GET-ADComputer -Identity "%s" -Properties *'%(cn)], stdout=sys.stdout, shell=True)
		# if ci < 20:
		if True:
			ci += 1
			p = subprocess.check_output(['powershell.exe', 'GET-ADComputer -Identity "%s" -Properties *'%(cn)], shell=True).decode("utf-8")

			p = p.split("\n")
			for l in p:
				if "Description" in l:
					l.replace(": -",":  -")
					m = l.split(" : ")[1]
					m = m.split(" - ")[0]

					print(">",m, cn)
					staffid = None
					if m != " " and m != "" and " " in m:
						print("m",m)
						rg = requests.get("http://workshop.cox.com.au/oj/api/staff_details.json/?search=%s"%(m))
						try:
							print(rg.json()[0])
							staffid = rg.json()[0]['id']
						except Exception as e: print(e)
					# if staffid:
					url = 'http://workshop.cox.com.au/oj/functions/edit/'
					myobj = {'data': [{"obtype":"hardware","key":"staff","value":staffid,"pk":"number","pv":cn}]}
					print(myobj)
					x = requests.post(url, data = json.dumps(myobj))
					print(json.dumps(x.json(),indent = 4))

rg = requests.get("http://workshop.cox.com.au/oj/api/hardwares.json/")
for h in rg.json():
	if h["number"] not in clist and h["elementType"] == 2:
		# print(h)
		url = 'http://workshop.cox.com.au/oj/functions/edit/'
		myobj = {'data': [{"obtype":"hardware","key":"staff","value":None,"pk":"number","pv":h["number"]}]}
		x = requests.post(url, data = json.dumps(myobj))
		# print(json.dumps(x.json(),indent = 4))