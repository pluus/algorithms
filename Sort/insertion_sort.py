import random

'''



	Insertion Sort


	Time Complexity : O(N^2)
	Space Complexity : O(N)
	Stability : O



'''
def insertionSortVer1(a):
	for i in range( 1, len(a) ):
		curPosition = i
		curValue = a[i]
		# Check previous values. If found any,
		while curPosition > 0 and curValue < a[curPosition-1]:
			# Shift elements
			a[curPosition] = a[curPosition -1]
			curPosition -= 1
		# Insert the value.
		# This could be something like a[:i] + curValue + a[....]  but this is python way.
		a[curPosition] = curValue


def insertionSortVer2(a):
	# Add sentinel. By having this, we don't need curPosition > 0 statement while looping
	a2 = [-99999999] + a
	for i in range( 2, len(a2) ):
		curPosition = i
		curValue = a2[i]
		# Notice curPosition > 0 is gone.
		while( curValue < a2[curPosition-1] ):
			a2[curPosition] = a2[curPosition -1]
			curPosition -= 1
		a2[curPosition] = curValue
	a2.pop(0)
	return a2


'''

	TODO

	Use binary search to pinpoint where to insert the value.
	This works because all the previous values are all sorted.

'''

def binary_search(arr, val, start, end): 
    # we need to distinugish whether we should insert 
    # before or after the left boundary. 
    # imagine [0] is the last step of the binary search 
    # and we need to decide where to insert -1 
    if start == end: 
        if arr[start] > val: 
            return start 
        else: 
            return start+1
  
    # this occurs if we are moving beyond left\'s boundary 
    # meaning the left boundary is the least position to 
    # find a number greater than val 
    if start > end: 
        return start 
  
    mid = (start+end)/2
    if arr[mid] < val: 
        return binary_search(arr, val, mid+1, end) 
    elif arr[mid] > val: 
        return binary_search(arr, val, start, mid-1) 
    else: 
        return mid 

def insertionSortVer3(a):
	for i in range(1, len(a)):
		currentValue = a[i]
		j = binary_search(a, currentValue, 0, i-1)
		# Insert the value. Python style.
        a = a[:j] + [currentValue] + a[j:i] + a[i+1:] 


a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
insertionSortVer1(a)
print(a)

a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
a = insertionSortVer2(a)
print(a)

a = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
insertionSortVer3(a)
print(a)


