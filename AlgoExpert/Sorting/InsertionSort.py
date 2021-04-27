# O(n^2) time | O(1) space
# 第一层从1开始loop， 第二层while loop指针从右往左插入

def insertionSort(array):
	n = len(array)
	for i in range(1, n):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
			j -= 1
	return array