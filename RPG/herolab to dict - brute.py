import xmltodict, json, collections

interestingList = ["@name","@abbr","@save", "@ranks", "@value","@summary",
"@ac",
"@touch",
"@flatfooted",
"@cmb",
"@cmd",
"@total",
"@baseattack",
"@hitpoints",
"@attack",
"@crit",
"@damage",
"@quantity",
"@typetext",
"@rangeincvalue",
"@classskill",
"specsource",
]
rootList = ["",
"skill",
"feat",
"classes",

"language",
"attribute",
"save",
"armorclass",
"maneuvers",
"initiative",
"attack",
"weapon",
"item",
"special",

]
rootKeys = [
"race",
"alignment",
"size",
"health",
]
interestingDicts = ["attrbonus",
"spelllevel",
"attrvalue",
"weight"
"speed",
"special"
]

def deepDive(object, root=[], rootOb = {}, kind="dict"):
	for k,v in object.items():
		if k in rootList and type(v) != type([]):
			v = [v]

		key = None
		run = False
		if type({}) == type(v):
			# key = k
			# print(k)
			if k in interestingDicts:
				key = k
				run = True
			else:
				deepDive(v, root+[k], rootOb)

		elif type([]) == type(v):
			# if k in rootList:
				# print(v)
			# key = k
			if k in interestingDicts:
				print("interestingDicts",k, )
				key = k
				run = True
			for i in v:
				forOb = {"elements":[]}
				if type({}) == type(i):
					deepDive(i, root+[k], forOb, "list")
				if forOb != {}:
					# print(forOb)
					rootOb["elements"].append(forOb)
		else:
			key = k
			# print(k)
		
		if key in interestingList and root[-1] in rootList: run = True
		if key in interestingList and root[-1] in rootKeys: run = True
		if run:
			# print(key)
			try:	key = key.replace("@","")
			except: key = "None"
			rootOb["rootList"] = root.copy()
			if kind == "dict":
				key = root[-1]+"_"+key 
			elif kind == "list":
				rootOb["type"] = root[-1]
			rootOb[key] = v

#### BRUTE
with open("fotrm.xml", 'r') as file:
	o = json.loads(json.dumps(xmltodict.parse(file.read())))
	# print(o)
	for charIndex,character in enumerate(o["document"]["public"]["character"]):
		print("-"*80)
		print("-"*80)
		charOb = {"elements":[]}
		deepDive(character,[""],charOb)
		for element in charOb["elements"]:
			# print(element)
			newKey=[]
			for k in ["type","name"]:
				try:	newKey.append(element[k])
				except: pass
			newKey = "_".join(newKey)
			charOb[newKey] = element
		for combListKey in ["weapon","feat","special", "item"]:
			apob = []
			for k,v in charOb.items():
				if combListKey in k:
					apob.append(v)
			charOb[combListKey+"_list"] = apob
		for joinListKey in [["language","name"]]:
			apob = []
			for k,v in charOb.items():
				if joinListKey[0] in k:
					apob.append(v[joinListKey[1]])
			charOb[joinListKey[0]+"_join"] = "; ".join(apob)
		charOb["special_list"]= charOb["feat_list"]+charOb["special_list"]
		try:	charOb["special_list"]= charOb["special_list"]+charOb["attack"]["special"]
		except:	pass
		for cO in charOb["special_list"]:
			try:	cO["name"] = cO["@name"]
			except:	pass
		charOb["special_list"] = list(filter(lambda x: "name" in x, charOb["special_list"]))
		with open("C:\\Users\\Andrew\\OneDrive - Cox Architecture Pty Ltd\\RPG\\"+str(charIndex)+".json","w") as file:
			text = json.dumps(charOb)
			text = text.replace("\\u00c3\\u2014","x")
			file.write(text)
		print(text)
	# print(json.dumps(o))