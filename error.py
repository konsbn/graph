def swap(tuplet):
	tuplet = (tuplet[1], tuplet[0])
	return tuplet
#################################################
def distinct(inlist):
	new_list = []
	for i in inlist :
		a  = (i in new_list) | (swap(i) in new_list)
		if a == False: 
			new_list.append(i)
	return new_list
#######################d
def elimsim(inlist):
	elimlist = distinct(inlist)
	for j in elimlist:
		if (j[0] == j[1]):
			elimlist.remove(j)
	return elimlist