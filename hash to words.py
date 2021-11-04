import string
import json

with open("D:\\Dropbox (COX Architecture)\\LOCAL TEMP\\wordsHash.json", "r") as f:
	data = json.load(f)

hashWord = "641270"
elementID = "641270"

hashWordList = list(hashWord)
charString = []
charIndex = 0
wordString = []

for i, c in enumerate(hashWordList):
	if i == int(len(hashWordList)/2) and charIndex < 3:
		charIndex = 3
	charString.append(c)
	if i % 2 == 1:
		lu = str(charIndex)+"_"+"".join(charString)
		wordString.append(data[lu])
		charString = []
		charIndex += 1
print(wordString)
