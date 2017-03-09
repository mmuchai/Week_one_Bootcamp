def words (statement):
	statement = statement.split()
	count = {}
	
	for word in statement:
		if word in count:
			count[word] += 1
		else:
			try:
				if type(int(word)) == int:
					count[int(word)] = 1
					continue
			except:
				count[word] = 1
	return count
	
N ='car : carpet as java : javascript!!&@$%^&'
words (N)