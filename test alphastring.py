def intToalphabet(intVal = 0, ignore=["I","O"]):
	import string
	alphabet = list(string.ascii_uppercase)
	for i in ignore:
		alphabet.remove(i)
	division = len(alphabet)
	def recurseBase(number, division, outindex = []):
		import math
		number = math.floor(number)
		result = number/division
		if result >= 1.0:
			outindex = recurseBase(((math.floor(result)))-1, division, outindex)
		remainder = (result-math.floor(result))*division
		remainder = int(round(remainder,0))
		outindex.append(remainder)
		return outindex
	letterIndexes = recurseBase(intVal, division)
	letters = list(map(lambda x: alphabet[x], letterIndexes))
	out = "".join(letters)
	return out