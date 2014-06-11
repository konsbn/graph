def degree(adj,node = None,all = False):
    import numpy as np
    import adjm as ad
    import nodes as nd
    idx = len(adj)
    degree = []
    for j in range(idx):
        temp = 0
        for i in range(idx):
            temp = temp + adj[j,i]
        degree.append(temp)
    if all == False:
    	return degree[node]
    if node == None:
    	if all ==  True:
		return degree
    
	
        
