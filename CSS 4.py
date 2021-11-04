def css_unpacking(css):
	import re
	cleanup = [(r'''\s+(?=(?:(?:[^"]*"){2})*[^"]*"[^"]*$)''','<!ws!>'), (r'''\s''',''),('<!ws!>',' '),(';}',';}<!css-split!>')]
	for c in cleanup:
		d = re.compile(c[0])
		css = d.sub(c[1], css)
	css_data = css.split("<!css-split!>")
	css_data = css_data[:-1]
	# print(css_data)

	cssarray = []
	for entry in css_data:
		regexs = re.search(r'^(.+?){(.+?)}$', entry, re.IGNORECASE)
		search = regexs.group(1)
		style = regexs.group(2)
		style = style.split(";")
		sdict = {}
		for s in style:
			try:
				kv = s.split(":")
				try:
					sdict[kv[0]] = eval(kv[1])
				except:
					sdict[kv[0]] = kv[1]
			except: pass
		outdict = {"search": search, "style": sdict}
		cssarray.append(outdict)
	return cssarray



def append(textToAppend, newline=True, key, new, old):
	try:
		apob = old[key]
	except:
		apob=""
	nl = ""
	if newline:
		nl = "\n"
	apob += nl+textToAppend
	new[key] = apob
	return new

def processFunctions(new, old):
	import re
	for k, v  in new.items():
		# print(k,v)
		reSearch = re.search(r'(^.+)\((.+)\)$', v)
		if reSearch:
			# print(reSearch.group(1))
			arg = eval(reSearch.group(2))
			new = globals()[reSearch.group(1)](arg, k, new, old)
	return new

def apply_css(d, css):
	cssarray = css_unpacking(css)
	# print(cssarray)
	outdict = {}
	for css_item in cssarray:
		try:
			# print(css_item["search"],eval(css_item["search"]))
			if eval(css_item["search"]):
				style = css_item["style"]
				style = processFunctions(style, outdict)
				outdict.update(style)
		except Exception as e: 
			print(e)
			pass
	outdict.update(d)
	return outdict


css = r'''
d["parent_room"]=="MECH OTHER"
	{
		from_side: append("Mechanical Room");
	}
d["from_room"]=="STAIR"
	{
		from_side: append("Exit to Level 2", False);
		to_side: append("FIRE STAIR EXIT");
	}
'''


door = {
	"to_room": "MECH OTHER",
	"from_room": "STAIR",
	"parent_room": "MECH OTHER",
}


door = apply_css(door, css)
print(door)