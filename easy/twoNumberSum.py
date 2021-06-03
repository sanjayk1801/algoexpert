def twoNumberSum1(array, targetSum):
	n = len(array)
	for i in range(n - 1):
		j = i + 1
		for k in range(j, n):
			sum = array[i] + array[k]
			if sum == targetSum:
			    return [array[i], array[j]]
	return []

def twoNumberSum2(array, targetSum):
    nums = []
    for i in array:
        potential_match = targetSum -  i
        if potential_match in nums:
            return [potential_match, i]
        else:
            nums.append(i)


def twoNumberSum3(array, targetSum):
    array.sort()
    



sol1 = twoNumberSum1([3, 5, -4, 8, 11, 1, -1, 6], 10)		

sol2 = twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10)	



