# O(N) time and space
# 一直把比stack[-1]小的值入栈，一旦发现大于它的值，把stack中index取出，存入result
def nextGreaterElement(array):
	n = len(array)
	result = [-1] * n
	stack = []

	for i in range(n * 2):
		index = i % n
		while stack and array[stack[-1]] < array[index]:
			result[stack.pop()] = array[index]
		stack.append(index)

	return result
