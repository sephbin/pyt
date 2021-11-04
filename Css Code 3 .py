master_css = '''

.rules{
	area>500:5 star;
	400<area<500:4 star;
	300<area<400:3 star;
	200<area<300:2 star;
	100<area<200:1 star;
	
	level>20:5 star;
	level>15:3 star;
	level>10:3 star;
	level>5:2 star;
	level>0:1 star;
}

.bedroom{
	ceiling: other;
	floor: good carpet;
	door: black;
}

.hallway{
	floor: timber;
	door: red;
	walls: red;
	windows: tall;
}
.test{
	hello: world;
	walls: yellow;
	floor: timber;
}
.bathroom{
	ceiling: MPB;
	floor: tile;
	walls: MPB;

}
.level<12{
	walls: level under 12;
}

.area<300{
	floor: less than 300;
	walls: less than 300;
}

.300<area<500{
	floor: less than 500;
	walls: less than 500;
}

.area>500{
	floor: more than 500;
	walls: more than 500;
}

.star>3{
	walls: silver;
	floor: timber;
}

.roof{
	ceiling: glass;
	floor: tile;
}

'''


# master_css = '''
# "bed" in d["class"]{
#     ceiling: other;
#     floor: good carpet;
#     door: black;
# }
# '''


def css_unpacking(css):
	import re
	try:
		file = open(css, mode='r')
		css = file.read()
		file.close()
	except: pass

	# Format file and sort into Master CSS dictionary

	css_data = css.replace('\n', '').replace(' ', '').replace('\t', '').replace(';}', ';}<!css-split!>')
	css_data = css_data.split("<!css-split!>")
	css_data = css_data[:-1]

	cssarray = []
	for entry in css_data:
		regex = re.search('^(.+?){(.+?)}$', entry, re.IGNORECASE)

		search = regex.group(1)
		print(search)
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

def logic(search):
	
	update_style = {}
	
	
	# CLASS SELECTORS
	
	for k, v in search.items():
		if k == 'class':
			css_class = v.split(',')
			for v in css_class:
				
				# All Elements
				if '*' in v:
					for i in cssarray:
						update_style.update(i["style"])
				
				# Element from Class
				elif v[0] != '.':
					search_style = v.split('.')
					element = search_style[0]
					element = element.replace(' ','')
					css_class = search_style[1]
					for i in cssarray:
						s = ''
						if s.join(i['search'][1:]) == css_class:
							for k,v in i['style'].items():
								if k == element:
									element_dic = {k:v}
									update_style.update(element_dic)
									print("Class: {} for element {} \nUpdate:".format(css_class.capitalize(),element.capitalize()), update_style,'\n')
				
				# Class1 + Class2 Descendents
				elif '. ' in v:
					search_style = v.split('. ')
					for css in search_style:
						if '.' in css:
							css_class = css.replace('.','')
							css_class_dic = {}
							for i in cssarray:
								s = ''
								if s.join(i['search'][1:]) == css_class:
									css_class_dic.update(i['style'])
									break
						else:
							css_descendents = css
							css_descendents_dic = {}
							for i in cssarray:
								s = ''
								if s.join(i['search'][1:]) == css_descendents:
									css_descendents_dic.update(i['style'])
									break
				
							for kc, vc in css_class_dic.items():
								for kd, vd in css_descendents_dic.items():
									if kc == kd:
										descendents_dic = {kc:vd}
										css_class_dic.update(descendents_dic)
										update_style.update(css_class_dic)
										print("Class: {} with element ({}:{}) from descendent {} \nUpdate:".format(css_class.capitalize(),kc.capitalize(),vd.capitalize(),css_descendents.capitalize()), update_style,'\n')

				# Class1 + Class2
				elif '.' in v:
					search_style = v.split('.')
					for i in cssarray:
						for x in search_style:
								s = ''
								if s.join(i['search'][1:]) == x:
									update_style.update(i["style"])
									print("Class: {} \nUpdate:".format(x.capitalize()), update_style,'\n')
		 
		
	# AREA 
	
	for k, v in search.items():
		if k == 'area':
			if v.isdigit():
				area = int(v)
				for css in cssarray:
					for k, v in css.items():
						if 'area' in v:
							if eval(v[1:]):
								update_style.update(css["style"])
								print("{} \nUpdate:".format(v[1:].title()), update_style,'\n')
			else:
				search[k] = 'Area Undefined'
	
	
	# LEVEL
				
	for k, v in search.items():
		if k == 'level':
			if v.isdigit():
				level = int(v)
				search[k] = 'Level {}'.format(level)
				for css in cssarray:
					for k, v in css.items():
						if 'level' in v:
							if eval(v[1:]):
								update_style.update(css["style"])
								print("{} \nUpdate:".format(v[1:].capitalize()), update_style,'\n')
			else:
				search[k] = 'Level Undefined'
	   
	
	# STAR RATING
	
	for k, v in search.items():
		if k == 'star':
			if v.isdigit():
				star = int(v)
				search[k] = '{} Star'.format(star)
				for css in cssarray:
					for k, v in css.items():
						if 'star' in v:
							if eval(v[1:]):
								update_style.update(css["style"])
								print("{} Star \nUpdate:".format(star), update_style,'\n')
			else:
				search[k]= 'Stars Undefined'

				
	# USER OVERRIDE
	
	for k, v in search.items():
		if v != '':
			if k != 'class' and k != 'star' and k != 'level' and k != 'area':
				user_dic = {k:v}
				update_style.update(user_dic)
				print("User Override: ({}: {}) \nUpdate:".format(k.capitalize(),v.capitalize()), update_style,'\n')

				
	search.update(update_style)
	
	return search

bedroom_4star = {
"class":".bedroom.test, ceiling.roof",
"star":"4",
"level":"10",
"area":"450",
"walls": "blue",
"door":"timber",
}

bedroom_3star = {
"class":".bedroom.test",
"star":"3",
"level":"",
"area":"350",
"walls": "blue",
"door":"timber"
}

bedroom_2star = {
"class":".bedroom. hallway",
"level":"10",
"star":"",
"area":"250",
"walls": "red",
"door":"wood"
}

bedroom_1star = {
"class":".hallway, floor.bedroom",
"level":"",
"star":"1",
"area":"",
"walls": "yellow",
"door":"orange"
}


print(logic(bedroom_2star))