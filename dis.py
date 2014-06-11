##This  module takes an array and returns the distinct values in ##another list

def distinct(a):
	temp = []
	for i in a:
		flag = i in temp
		if flag == False:
			temp.append(i)

	return temp
