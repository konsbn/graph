def is_edge(adjm, edge ):
		flag  = True
		edge =  (edge[0] , edge[1])
		#print edge
		if adjm[edge] == 1:
			flag = flag & True
		edge =  (edge[1],edge[0])
		if adjm[edge] == 1:
			flag = flag & True
		else:
			flag = flag & False
		return flag