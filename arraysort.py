

# Using Default dictionary (works as Multimap in Python)
from collections import defaultdict
def rearrange(a, n, val):
	# initialize Default dictionary
	dict = defaultdict(list)
	
	# Store values in dictionary (i.e. multimap) where,
	# key: absolute difference between 'val'
	# and array elements (i.e. abs(val-a[i])) and
	# value: array elements (i.e. a[i])
	for i in range(0, n):
		dict[abs(val-a[i])].append(a[i])
	
	index = 0
	
	# Update the values of original array
	# by storing the dictionary elements one by one
	for i in dict:
		
		pos = 0
		while (pos<len(dict[i])):
			a[index]= dict[i][pos]
			index+= 1
			pos+= 1
	
# Driver code	
a =[7, 12, 2, 4, 8, 0]
val = 6

# len(a) gives the length of the list
rearrange(a, len(a), val)

# print the modified final list
for i in a:
	print(i, end =' ')
