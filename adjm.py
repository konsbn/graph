def make_adjacency(edges):
	import numpy as np
	import nodes as nd
	nods = nd.node(edges)
	size  = len(nods)
	adjm = np.zeros((size,size))
	#print adjm
	for i in edges:
		c = (i[0], i[1])
		d = (i[1], i[0])
		#print c
		adjm[c] = 1
		adjm[d] = 1
	return adjm
	
