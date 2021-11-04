
import subprocess
import sys
import re
import requests
import json
from fuzzywuzzy import fuzz, process

clist = ["SYD-NB-254","SYD-NB-255","SYD-NB-256"]

for c in clist:
	try:
		p = subprocess.check_output(['powershell.exe', r'ping -n 1 %s'%(c)], shell=True).decode("utf-8", errors="ignore")
		if "unreachable" not in p:
			p = subprocess.check_output(['powershell.exe', r'C:\PSTools\PsLoggedOn \\%s'%(c)], shell=True).decode("utf-8", errors="ignore")
			p = p.split("\r\n")
			for l in p:
				if "COXGROUP" in l:
					print(l)
	except:
		print(c,"ping failed")
		pass
