import networkx as nx
G = nx.MultiDiGraph()
class ob:
	graphOb = {"id":"-"}
	def __init__(self, d={}):
		self.graphOb = d
	def __repr__(self):
		# import json
		# return json.dumps(self.graphOb)
		return self.graphOb["id"]

A = ob({"id":"A"})
B = ob({"id":"B"})
C = ob({"id":"C"})
D = ob({"id":"D"})
# G.add_nodes([A,B,C,D])
# G.add_edge(A, B)
# G.add_edge(B, C)
# G.add_edge(B, D)
G.add_edges_from([
	(0, 1, {"step":1, "weight":10.0, "colour":"red"}),
	(1, 2, {"step":1, "weight":10.0, "colour":"red"}),
	(2, 3, {"step":1, "weight":10.0, "colour":"blue"}),
	(3, 0, {"step":1, "weight":10.0, "colour":"red"}),
	(3, 2, {"step":100, "weight":1.0, "colour":"blue"}),
	(2, 0, {"step":10, "weight":1.0, "colour":"blue"}),
	])
# print(G.nodes)
# print(G.edges.data())

def filterByKey(u, v, d):
	# print("u",u)
	# print("v",v)
	# print("d",d)
	return 1 if d[0]['colour']=="red" else None


# print(nx.dijkstra_path(G,3,0, 'weight'))
print(nx.single_source_dijkstra_path(G,3))
print(nx.single_source_dijkstra_path(G,3,weight="step"))
# print(nx.single_source_dijkstra_path(G,3,weight = lambda u, v, d: 1 if d[0]['colour']=="red" else None))
print(nx.single_source_dijkstra_path(G,3,weight = lambda u, v, d: filterByKey(u,v,d)))
# for i in nx.all_shortest_paths(G,3,0):
	# print(i)