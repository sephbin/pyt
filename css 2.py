master_css = r'''
"bed" in d["class"]{ceiling: other; floor: good carpet; door: black; }
"other" in d["class"]{ceiling: other; floor: ASas carpet; door: dAD; }
"A" in d["class"]{X:1; Y:2; Z:3;}
"B" in d["class"]{X:4; Y:5; Z:6;}
"B" in d["class"] and  "ROOF" in d["class"]{Z:GLASS CEILING; k:call(http:\\www.google.com)}
re.search(r"\bB\b",d["class"]){X:10; Y:11; Z:12;}

d["area"] > 300{hello:world; }

'''

import re
def css_unpacking(css):
	try:
		file = open(css, mode='r')
		css = file.read()
		file.close()
	except: pass

	# Format file and sort into Master CSS dictionary

	css_data = css.replace('\n', '').replace('\t', '').replace('}', '}<!css-split!>')#.replace(' ', '')

	# [^][^{]+{[^}]+?}
	css_data = css_data.split("<!css-split!>")
	css_data = css_data[:-1]
	# print(css_data)

	cssarray = []
	for entry in css_data:
		regex = re.search('^(.+?){(.+?)}$', entry, re.IGNORECASE)

		search = regex.group(1)
		# print(search)
		style = regex.group(2)
		style = style.split(";")
		sdict = {}
		for s in style:
			try:
				kv = s.split(":")
				sdict[kv[0]] = kv[1]
			except: pass
		outdict = {"search": search, "style": sdict}
		cssarray.append(outdict)
	return cssarray

cssarray = css_unpacking(master_css)
# print(cssarray)

obs = [
{"class":"A B", "level":"", "star":"1", "area":500, "walls": "yellow", "door":"orange"},
{"class":"B", "level":"10", "star":"", "area":150, "walls": "red", "door":"wood"},
{"class":"B ROOF", "level":"10", "star":"", "area":150, "walls": "red", "door":"wood", "Z":"LAVA"}
]

finishedobs = []
for ob in obs:
	d = ob
	outdict = {}
	for css_item in cssarray:
		try:
			print(css_item["search"],eval(css_item["search"]))
			if eval(css_item["search"]):
				# print("applying %s"%(css_item["search"]))
				# print(outdict, css_item["style"])
				outdict.update(css_item["style"])
				# print(outdict)
		except Exception as e: 
			print(e)
			pass
	# print("BEFORE UPDATE",outdict)
	outdict.update(ob)
	# print("BEFORE APPEND",outdict)
	finishedobs.append(outdict)

print(finishedobs)
