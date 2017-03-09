class BinarySearch (List):
	def __init__ (self, a ,b):
		''' The length of a list and the step, give the endpoint of a range.
		'''
		super (BinarySearch, self).__init__(length)
		array_ = [num for num in range (0, (a*b)+1 ,b)]
		self.length = len(array_) = self.a
		self.extend(array_)

    def search(self, value):
        count = 0
        first = 0
        last = len(self) - 1
            
        if value == self[first]:
        	return {'count': count, 'index': first}
        elif value == self[last]:
        	return {'count': count, 'index': last}

        	midpoint = (first + last) // 2