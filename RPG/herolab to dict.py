import xmltodict, json, collections

with open("fotrm.xml", 'r') as file:
	o = json.loads(json.dumps(xmltodict.parse(file.read())))
	# for k,v in o["document"]["public"]["character"][1].items():
	# 	if type(v) == type(collections.OrderedDict()):
	# 		v = json.dumps(v)[:50]
	# 	print(k+":\t", v)
	print(o)
	char = o["document"]["public"]["character"][0]
	for k in char["attributes"]["attribute"]:
		print(k["@name"], k["attrvalue"]["@text"], k["attrbonus"]["@text"], )

	print("-"*20)
	print("AC", char["armorclass"]["@ac"], char["armorclass"]["@touch"], char["armorclass"]["@flatfooted"])
	print("-"*20)
	for k in char["saves"]["save"]:
		print(k["@abbr"], k["@save"],)

	print("-"*20)
	for k in char["melee"]["weapon"]:
		print(k["@name"],
			k["@attack"],
			k["@damage"],
			)
	try:
		if type(char["ranged"]["weapon"]) != type([]):
			char["ranged"]["weapon"] = [char["ranged"]["weapon"]]
		for k in char["ranged"]["weapon"]:
			print(k["@name"],
				k["@attack"],
				k["@damage"],
				)
	except: pass
	print("-"*20)
	for k in char["skills"]["skill"]:
		print(
			k["@name"],
			k["@value"],
			k["@ranks"],

			)
	print("-"*20)
	try:
		for k in char["feats"]["feat"]:
			print(
				k["@name"],
				)
	except: pass
	try:
		if type(char["otherspecials"]["special"]) != type([]):
				char["otherspecials"]["special"] = [char["otherspecials"]["special"]]
		for k in char["otherspecials"]["special"]:
			print(
				k["@name"],
				)
	except: pass
	try:
		if type(char["weaknesses"]["special"]) != type([]):
				char["weaknesses"]["special"] = [char["weaknesses"]["special"]]
		for k in char["weaknesses"]["special"]:
			print(
				k["@name"],
				)
	except: pass
	try:
		if type(char["attack"]["special"]) != type([]):
				char["attack"]["special"] = [char["attack"]["special"]]
		for k in char["attack"]["special"]:
			print(
				k["@name"],
				)
	except: pass
	try:
		if type(char["defenses"]["special"]) != type([]):
			char["defenses"]["special"] = [char["defenses"]["special"]]
		for k in char["defenses"]["special"]:
			print(
				k["@name"],
				)
	except: pass




	print("#"*80)
	
	print(char["defenses"])
	print("#"*80)

	for k,v in char.items():
		print(k)
	var = char["attributes"]["attribute"]
		
	# print(char["attributes"])