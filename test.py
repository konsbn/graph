def neighbors(adjm, node):
	import is_edge
	nbors  = []
	for l in range(len(adjm)):
		edge = (node,l)
		if is_edge.is_edge(adjm,edge):
			nbors.append(edge)
		newlist = nbors
	nbors = newlist
	# if edge == False:
	# 	return nbors
	# if edge ==True:
	# 	nbors = strip(nbors)
	# 	return nbors
	return nbors

def strip(inlist):
	newlist = []
	for i in inlist:
		newlist.append(i[1])
	return newlist

def recurse(adjm, node):
	list2 = []
	list2 = neighbors(adjm, node, True)
	for i in list2:
		recurse(adjm, i)
	return list2
