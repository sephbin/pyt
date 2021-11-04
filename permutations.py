# A Python program to print all  
# permutations using library function 
from itertools import combinations 

mainlist = {"A":"A","B":"B","C":"C"}
keys = list(mainlist)

length =len(mainlist)
outdicts = []
for l in range(length+1):
	print(l)
	perm = combinations(list(range(length)), l) 
	# Print the obtained permutations 
	for i in list(perm): 
		print("i",i)
		alterdict = dict(mainlist)
		for index in i:
			alterdict[keys[index]] = None
		outdicts.append(alterdict)
print(outdicts)