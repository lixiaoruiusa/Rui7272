# O(n^2) time | O(1) space

def bubbleSort(array):
    n = len(array)
    # range(n) also work but outer loop will repeat one time more than needed.
	for i in range(n - 1):
		# Last i elements are already in place
		for j in range(n - 1 - i):
			if array[j] > array[j + 1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array
