import random

'''



	Bubble Sort




'''

def bubbleSortVer1(a):

	# step is -1 because everytime something is sorted via buble sort, it will be placed in the last.
    for i in range( len(a) -1, 0, -1 ):
    # check the range
        for j in range( i ):
    # swap values
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp


def bubbleSortVer2(b):

	for i in range( len(a) - 1, 0, -1 ):
		# Check if the array is sorted
		is_sorted = True

		for j in range(i):
			if( a[j] > a[j+1] ):
				t = a[j]
				a[j] = a[j+1]
				a[j+1] = t
				# swapped at least once? The array is not sorted yet. Keep gonig
				is_sorted = False
				
		# Never swapped? It means the array is sorted!
		if( is_sorted ):
			break



a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

random.shuffle(a)
bubbleSortVer1(a)
print(a)

random.shuffle( a )
bubbleSortVer2(a)
print(a)






