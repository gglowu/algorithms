#point class is used to store related information of pixels which can be applied to Astart algorithm to find the shortest route.
#x: the x position of the pixel in  picture
#y: the y position of the pixel in  picture
#G: the cost of path from the start pixel to current pixel
#H:	the heuristic shortest path from current pixel to end pixel
#ptype:the type of the pixel, to map the cost of current pixel
#parent: the parent pixel of current pixel, so can track the path back from end point to start point
#in_openlist: if current pixel is in openlist
#in_closelist: if current pixel is in closelist

class point(object):
	"""docstring for point"""
	def __init__(self, pointx, pointy):
		self.x = pointx
		self.y = pointy
		self.F = 0
		self.G = 0
		self.H = 0
		self.ptype = 0
		self.parent = None
		self.in_openlist = False
		self.in_closelist = False

	#overwrite _lt_ operator so can use insort_left to manage openlist
	def __lt__(self, other):
		return self.F > other.F or (self.F == other.F and self.G < other.G)