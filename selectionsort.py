import random

a = [random.randrange(0,10000) for p in range (0,101)]

def selectionsort(arr):
	for index in range(0,len(arr)):
		print index
		temp = index;
		for newindex in range(index,len(arr)):
			if arr[newindex] < arr[temp]:
				temp = newindex;
		if index != temp:
			temp2 = arr[index]
			arr[index] = arr[temp]
			arr[temp] = temp2
	return arr

print selectionsort(a);
