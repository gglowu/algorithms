#Class network implements a set of functions to find a shortest path in a point matrix from start point to end point.
#timecost: map pixel types to path cost
#maze: point matrix of PNG
#width: width of point matrix
#height: height of point matrix

from point import *
from bisect import insort_left

class network():
	def __init__(self, timecost, maze):
		self.timecost = timecost
		self.maze = maze
		self.width = len(maze)
		self.height = len(maze[0])


#calculate the G cost from current point to target point
	def calG(self, current, target):
		extraG = self.timecost[target.ptype]
		preG = current.G
		return extraG + preG

#calculate the H cost from current point to target point (Manhattan distance has been applied here)
	def calH(self, current, target):
		return abs(current.x - target.x) + abs(current.y - target.y)

# F = H + G
	def calF(self, current):
		return current.H + current.G

#check all the adjacent points around current point and add those which current point can reach to into a point list, then return the list
	def getSurroundPoints(self, current):
		points = []
		for i in range(current.x-1, current.x+2):
			for j in range(current.y-1, current.y+2):
				if i >=0  and i <= self.width -1 and j >=0 and j <= self.height-1:
					target = self.maze[i][j]
					if self.isCanreach(current, target) == True:
						points.append(target)
		return points

#check if the current point can get to the target point
	def isCanreach(self, current, target):
		if target.ptype == 0 or target.in_closelist == True  or (current.x == target.x and current.y == target.y):
			return False
		elif abs(target.x - current.x) + abs(target.y - current.y) == 1:
			return True
		else:
			return False

#use Astar algorithm to find a shortest path in self.maze, from startpoint to endpoint. 
	def findPath(self, startpoint, endpoint):
		openlist = []
		openlist.append(startpoint)
		while openlist != []:
			current = openlist.pop()
			current = self.maze[current.x][current.y]
			current.in_openlist = False
			current.in_closelist = True

			if current.x == endpoint.x and current.y == endpoint.y:
				return current

			surroundpoints = self.getSurroundPoints(current)
			for target in surroundpoints:
				target = self.maze[target.x][target.y]
				if target.in_openlist == False:
					target.parent = current
					target.G = self.calG(current, target)
					target.H = self.calH(target, endpoint)
					target.F = self.calF(target)
					insort_left(openlist, target)
					target.in_openlist = True;
				else:
					tmpG = self.calG(current, target)
					if tmpG < target.G:
						target.parent = current
						target.G = tmpG
						target.F = self.calF(target)
		return None

#track the way back from end point to start point by using point.parent, then should be able to find the shortest path and return it
	def getPath(self, startpoint, endpoint):
		result = self.findPath(startpoint, endpoint)
		path = []
		while result != None:
			path.append(result)
			result = result.parent

		return path