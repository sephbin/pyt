d = {"office": ["offices", "loan_office", "office", "headquarters", "ticket_booth", "home_office", "main_office", "shipping_office", "countinghouse", "life_office", "business_office", "box_office", "government_office", "newsroom", "central_office", "home_base", "ticket_office"],
"tv_studio": ["newsroom", "studio"], "hq":["headquarters"]}

rd = {}

for k,v in d.items():
	# print(k)
	for i in v:
		#Test meaning distance between i and k
		meaningdistance = 0.5
		if not i in rd:
			rd[i] = [(k,meaningdistance)]
		else:
			rd[i] += [(k,meaningdistance+.3)]

# print(rd)

fuzzylist = list(rd)
# print(fuzzylist)

matchedword = "headquarters"
matchedsyn = rd[matchedword]
m = sorted(matchedsyn, key=lambda x: x[1])
top = m[-1][0]
print(top)

