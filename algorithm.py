#from bisect import bisect_left, bisect_right 
from array import array

def values_between(input_array, a, b):
	#range(a,b) 
	#start = bisect_right(input_array,a)
	#end = bisect_left (input_array,b)
	#for i in input_array:
	#	print i
	#	total = total+i
	out_array = []
	if (a == b): return -1
        if (a>b): 
		print 'The first element should be smaller than the second one'
		return -1
	for i in input_array:
		if (int(i) >int(a)  and int(i) < int( b)):
			out_array.append(i)
			print 'appending to array'
                else:
			exit
	print 'result is' + str(out_array)
	return (out_array)

