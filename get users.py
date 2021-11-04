import subprocess
print("gogogo")
computers = [
"COX-RD-007",
"COX-RD-001",
"COX-RD-002",
"COX-RD-008",
"COX-RD-009",
"COX-RD-012",
"COX-RD-006",
"COX-RD-015",
"COX-RD-016",
"COX-RD-017",
"COX-RD-018",
"COX-RD-019",
"COX-RD-020",
"COX-RD-021",

]
for c in computers:
	try:
		print(c)
		x = subprocess.call('query user /server:%s'%(c),shell=True)
		print(type(x),x)
	except Exception as e:
		print(e)