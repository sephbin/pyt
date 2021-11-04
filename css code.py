

# Open/read CSS file
# Slicing/split file into sections
# Place in dictionary

#Receive Json file with keys, add values to them based off CSS
#CSS chooses based off certain properties/attributes from Json file

#Output updated Json file

string = '''

.bedroom{
	ceiling: other;
	floor: "good carpet";
}

.hallway{
	floor: timber;
}
.test{
	hello: world;
}
.bedroom.test{
	hello: universe;
}
.bathroom{
	ceiling: MPB;
	floor: tile;
	walls: MPB;

}
.level<5{
	class: append("3-star");
}

'''


def css_unpacking(css):
	import re
	try:
		file = open(css, mode='r')
		css = file.read()
		file.close()
	except: pass

	#Format file/clean up + sorts into master dictionary

	css_data = css.replace('\n', '').replace(' ', '').replace('\t', '').replace(';}', ';}<!css-split!>')
	css_data = css_data.split("<!css-split!>")
	css_data = css_data[:-1]

	cssarray = []
	for entry in css_data:
		regex = re.search('^(.+?){(.+?)}$', entry, re.IGNORECASE)

		search = regex.group(1)
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
	#css_dic = dict(x.split("{") for x in css_data.split("."))

	#Split sub-sections into dictionary

def buildlogic(search):
	#genreate string
	string = '''"bedroom" in cssobject["class"].split(" ")'''
	return string

def applycss(cssobject, cssarray):
	finalStyle= {}
	for css in cssarray:
		# print(css["search"])
		searchfunc = eval(buildlogic(css["search"]))
		if searchfunc:
			finalStyle.update(css["style"])
			print("fs", finalStyle)
	finalStyle.update(cssobject)
	return finalStyle
# for k, v in css_dic.items():
		 
	#css_dic[k] = dict(v.split(':') for v in css_data.split(";"))
	# print(k, v)


cssarray = css_unpacking(string)
print(cssarray)

obj = {
"class":"bedroom test",
"something":"else",
"walls": "SOLID GOLD"
}

a = applycss(obj, cssarray)
print(a)