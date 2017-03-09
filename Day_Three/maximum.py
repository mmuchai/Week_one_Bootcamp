'''An array containing the min and max number respectively'''
def find_max_min(numbers_list):
	min_number = numbers_list[0]
	max_number = numbers_list[0]
	for num in numbers_list:
		if num < min_number:
			min_number = num
		elif num > max_number:
			max_number = num
	if min_number == max_number: #Checks if the array has the same numbers. Returns the length in a list.
		return [len(numbers_list)]
	return [min_number, max_number]
A = [90,87,4,56,12]
print (find_max_min (A))
B = [5,5,5]
print (find_max_min(B))