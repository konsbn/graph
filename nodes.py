def node(edges, length = False):
	names = []
	for i in edges:
		names.append(i[0])
		names.append(i[1])
	nodes = []
	for j in names:
		flag = j in nodes
		if flag == False:
			nodes.append(j)
	new = nodes.sort()
	if length == True:
		return len(nodes)
	else:
		return nodes

