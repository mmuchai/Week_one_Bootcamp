def find_missing(array_one, array_two):
	the_difference = set(array_one) ^ set(array_two)
	if (isinstance (array_one, list) and isinstance(array_two, list) == [ ]:
		return 0
	elif array_one == array_two:
		return 0
	else:
		return (list(the_difference) [0])