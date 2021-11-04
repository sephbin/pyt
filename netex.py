class graph:
	
	graphOb = {}
	def __init__(self, a=[], b=[]):
		self.graphOb["nodes"] = a
		self.graphOb["edges"] = b

	def __repr__(self):
		import json
		return json.dumps(self.graphOb)
	@property
	def nodes(self):
		return self.graphOb["nodes"]
	@property
	def edges(self):
		return self.graphOb["edges"]
	# @property
	# def edges(self):
	# 	return self.graphOb["edges"]


x = graph(["A","B","C"], [(0,1),(1,2)], )
print(x.nodes)
print(x.edges)
# print(x)