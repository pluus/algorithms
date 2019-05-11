import random

'''



	Insertion Sort


	Time Complexity : O(N^2)
	Space Complexity : O(N)
	Stability : X


'''
def selectionSortVer1(a):
	for i in range( 0, len(a) - 1 ):
		minValue = a[i]
		minIndex = i

		for j in range( i+1, len(a) ):
			if( a[j] < minValue ):
				minValue = a[j]
				minIndex = j

		#swap
		a[minIndex] = a[i]
		a[i] = minValue

a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
selectionSortVer1(a)
print(a)
