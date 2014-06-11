def openfile(path):
	import nodes as nd
	import csv
	with open(path) as f:
		edges = [tuple(line) for line in csv.reader(f)]
	labels = nd.node(edges)
	idxs = dict(zip(labels, range(len(labels))))
	iedges = [(idxs[e[0]], idxs[e[1]]) for e in edges]
	return iedges