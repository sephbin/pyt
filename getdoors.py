import requests

url = 'http://labs.cox.com.au/bd/doors.json/?project__number=218018.00'

r = requests.get(url)
# print(r.json())

def wf(k,v,s="" ):
	global index
	f = s+k
	include = ["element_id", "Location", "Level","Family","file","Fire_"]
	run = False
	# print(f)
	for i in include:
		if i in f:
			run = True
	if run:
		f = f.replace("/","--")
		f = f.replace(":","++")
		if index == 0:
			fr = "w"
		else:
			fr = "a+"
		# print(fr)
		with open("D:\\Users\\s-abutler\\Downloads\\%s.txt"%(f),fr) as write_file:
			v = str(v).replace("218018.00|","")
			v = str(v).replace("[[[","")
			v = str(v).replace("]]]","")
			write_file.write(v)
			write_file.write("\t")
		index += 1

def wd(d, s=""):
	for k,v in d.items():
		if type(v) == type({}):
			wd(v,k+"__")
		else:
			wf(k,v,s)

for l in r.json():
	# print(l["id"])
	global index
	index = 0
	if "Location" in l["data"]:
		wd(l)