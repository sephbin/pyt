import string
import json

chars = list("1234567890"+string.ascii_lowercase)
# print(chars)
charList = []
for a in chars:
	for b in chars:
		charList.append(a+b)

hashDict = {}

with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\adjectives.txt") as fp:
	lines = fp.readlines()
	for i in range(3):
		for index, c in enumerate(charList):
			index = (int(index*3.5918))+i+1
			word = lines[index].replace("\n","")
			hashDict[str(i)+'_'+c] = word
			print(index, word)
with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\nouns.txt") as fp:
	lines = fp.readlines()
	for i in range(5):
		for index, c in enumerate(charList):
			index = (int(index*5.24))+i
			word = lines[index].replace("\n","")
			hashDict[str(i+3)+'_'+c] = word
			print(index, word)



with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\wordsHash.json", "w") as f:
	f.write(json.dumps(hashDict))