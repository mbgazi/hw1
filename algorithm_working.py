#from bisect import bisect_left, bisect_right 
from array import array

def values_between(array, arg1, arg2):
	#range(a,b) 
	#start = bisect_right(input_array,a)
	#end = bisect_left (input_array,b)
	#for i in input_array:
	#	print i
	#	total = total+i
	count = 0
        print 'input array is' + str(array)
        print 'arg2 is ' + str(arg1)
	print 'arg2 is ' + str(arg2)
#	out_array = []
#	if (a == b): return 0
 #       if (a>b): 
#		print 'The first element should be smaller than the second one'
#		return 0
	for i in array:
		print 'i is ' + str(i)
		if (int(i) > int(arg1)  and int(i) < int(arg2)):
#			out_array.append(i)
               		count = count+1
			print 'count is' + str(count)
	        else:
			print 'I am in else cond'
			exit
	return (count)

