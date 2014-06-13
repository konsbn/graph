class graph(object):
	
	def __init__(self, edges):
		import nodes as nd
		self.nodes = nd.node(edges)
		self.edges = edges

	def __str__(self):
		return "greated graph with nodes %s and %s edges " %(self.nodes, self.edges)

def adj_list(graph):
	edges = graph.edges
	nodes = graph.nodes
	adj = {}
	for i in edges:
		new_key = i[0]
		add_key = i[1]
		if new_key in adj:
			adj[new_key].append(add_key)
		else:
			adj[new_key] = [add_key]
	return adj

def filter(graph):
	adj = adj_list(graph)
	nodes = graph.nodes
	for i in nodes:
		if i not in adj:
			adj[i] = None
	return adj



def dfs_visit( adj, s, parent = {}):
	
	if parent == {}:
		parent[s] = None
	try:	
		for v in adj[s]:
			if v not in parent:
					parent[v] = s
					dfs_visit( adj, v, parent)
	except TypeError:
		pass
	return parent

def dfs(adj,v):
	parent = {}
	for s in v:
		if s not in parent:
			parent[s] = None
			dfs_visit(adj, s, parent)
	return parent