import math

class Point(object):
	def __init__(self, X, Y, name):
		self.x = X
		self.y = Y
		self.name = name

	def __str__(self):
		return "Point(%s,%s)"%(self.x, self.y)

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self,other):
		return (self.x == other.x and self.y == other.y)

	def __ne__(self, other):
		return not(self == other)

	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return math.sqrt(dx**2 + dy**2)
