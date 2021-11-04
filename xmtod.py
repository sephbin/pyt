import json
import xmltodict
with open("D:\\Users\\s-abutler\\Downloads\\GURPS\\GURPS 4e\\GURPS 4e Character Assistant\\Chars\\Sten\\Sten (Owen).gca4.XML") as xml_file:
	dd = xmltodict.parse(xml_file.read())


d = dict(dd["Character"]["Traits"])

# for t in d["Attribute"]:
	# try:	print(t["name"],t["score"])
	# except:	pass
	# if t['name'] == "ST":
	# 	for k, v in t.items():
	# 		print(k,":",v)

for t in d["Skill"]:
	a = {"nameext":None}
	a.update(t)
	print("{name} ({nameext}): {level}".format(**a) )
	# print(t["name"],
	# t["nameext"],
	# t["level"])
	# level
	# name
	# nameext
	# for k, v in t.items():
	# 	print(k,":",v)\
