def neighbors(adjm, node):
	import is_edge
	nbors  = []
	for l in range(len(adjm)):
		edge = (node,l)
		if is_edge.is_edge(adjm,edge):
			nbors.append(edge)
	return nbors

def strip(inlist):
	newlist = []
	for i in inlist:
		newlist.append(i[1])
	return newlist

def largest_component(adjm):
	neighbrs = []
	for i in adjm:
		nbrs = neighbors(adjm, i)
		if (len(nbrs) == 1):
			continue
		neighbrs.append(nbrs)
		new = strip(neighbrs)
		for j in new:
			new_neigh = neighbors(adjm, j)
			if (len(new_neigh) == 1):
			continue
			for lc in new_neigh:
				neighbrs[i].append(lc)
	return neighbrs

