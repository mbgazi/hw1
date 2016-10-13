from array import array

def values_between(input_array, a, b):

	out_array = []
	if (a == b): return -1
        if (a>b): 
		print 'The first element should be smaller than the second one'
		return -1
	for i in input_array:
		if (int(i) >int(a)  and int(i) < int( b)):
			out_array.append(i)
	        else:
			exit
	return (out_array)

