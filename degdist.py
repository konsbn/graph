##This function takes degree list and node_degree list and returns a ##list of how many nodes have the same degree 
def foo(degree, node_degree):
	import dis
	temp = []
	for i in node_degree:
		temp.append(i[1])
	dist = []
	for j in degree:
		klu = temp.count(j)
		dist.append(klu)
	degdist = zip(degree, dist)
	degdist = dis.distinct(degdist)
	return degdist
