def clustering(adjm, node):
	import degree as dg
	import nodes as nd
	import is_edge 
	import distinct as ds
	#import pdb
	idxs  = len(adjm)
	nbor = []
	#node = node -1
	for i in range(idxs): 				##nbor is the array of neighbor nodes
		if adjm[node ,i] == 1:
			nbor.append(i)

	flag = True
	#pdb.set_trace()
	conode = float(dg.degree(adjm,node))
	pos_edge = (conode*(conode -1)/2)
	edges = 0.0
	pre_edges = []
	for l in nbor:
		for k in nbor:
			temp = (l,k)
			pre_edges.append(temp)
	pre_edges = ds.elimsim(pre_edges)
	#print pre_edges
	for lc in pre_edges:
		if (adjm[lc] == 1):
			edges = edges +1
	if pos_edge == 0:
		cc= 0
	else:
		cc = (edges / pos_edge)

	return cc

def avg_clustering(adjm, nodelist):
	#import nodes as nd
	#n = nd.node(edges)
	avcc = 0.0
	for loc in nodelist:
		avcc = avcc + clustering(adjm, loc)
	avcc = (avcc/ len(nodelist))
	return avcc



