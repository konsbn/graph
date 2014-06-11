class graph(object):
	
	def __init__(self, edges):
		import nodes as nd
		self.nodes = nd.node(edges)
		self.edges = edges

	def __str__(self):
		return "greated graph with nodes %s and %s edges " %(self.nodes, self.edges)

def adj_list(graph):
	edges = graph.edges
	adj = {}
	for i in edges:
		new_key = i[0]
		add_key = i[1]
		if new_key in adj:
			adj[new_key].append(add_key)
		else:
			adj[new_key] = [add_key]
		# if new_key in adj.keys() == True:
		# 	adj[new_key].append(add_key)
		# if new_key in adj.keys() == False:
		# 	adj[new_key] = [add_key]
	return adj

#def seen()
