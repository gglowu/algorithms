class CircularArray(object):
	"""docstring for CircularArray"""
	def __init__(self, size):
		super(CircularArray, self).__init__()
		self.size = size
		self.__items = [None for x in range(size)]
		self.__head = 0

	def convert(self, index):
		if index < 0:
			index += len(self.__items)
		return (head + index) % len(self.__items)
	
	def rotate(self, shiftright):
		self.__head = convert(shiftright)

	def get(self, index):
		if index <0 || index >= len(self.__items):
			print("out of range")
			return False
		return self.__items[self.convert(index)]

	def set(self, index, newitem):
		self.__items[convert(index)] = newitem

#######################################################
class CircularArrayIterator(object):
	"""docstring for CircularArrayIterator"""
	def __init__(self, circulararray):
		super(CircularArrayIterator, self).__init__()
		self.__items = circulararray.__items
		self.__index = 0
		self.__size = len(self.__items)

	def __iter__(self):
		return self

	def __next__(self):
		if self.__index >= self.__size:
			return StopIteration
		self.__index += 1
		return self.__items[self.__index-1]
#######################################################
## array = CircularArray(10)
## iter = CircularArrayIterator(array)
## for obj in iter:
##    print(obj)


