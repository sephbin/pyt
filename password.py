import json

file = r"C:\Users\s-abutler\Downloads\dictionary.json"
edd = {}
with open(file, 'r') as f:
    edd = json.load(f)
nums = [1,2,3,4,5,6,7,8,9]
sufr = [1,2,3,4,5,6,7,8,9]

print(edd["halloo"])
for k1 in edd:
	for k2 in edd:
		for k3 in edd:
			print(k1+k2+k3)
			# for r in sufr:
				