def ck(adjm,nodes):
	import clustering as cl 
	import degree as dg 
	dist = {}
	for j in nodes:
		deg = dg.degree(adjm,j)
		cls = cl.clustering(adjm, j)
		if if_present(deg, dist) == False:
			dist[deg] = [cls]
		if if_present(deg, dist) == True:
			dist[deg].append(cls)
	dist = popit(dist)
	# dist = ckdist(dist)
		#dist[deg] = cls
	return dist
def if_present(key, dictionary):
	flag = key in dictionary.keys()
	return flag
def pop(listi):
	 listi = listi[1:]
	 return listi

def popit(dictionary):
	for i in dictionary:
		dictionary[i] = pop(dictionary[i])
	return dictionary
def ckdist(dictionary):
	import pdb
	pdb.set_trace()
	degrees = dictionary.keys()
	cluc = []
	avg = 0
	for i in dictionary:
		coeff = dictionary[i]
		for j in coeff:
			avg = avg + j
		avg = avg/len(coeff)	
		cluc.append(avg)
	new  = zip(degrees,cluc)

	return new