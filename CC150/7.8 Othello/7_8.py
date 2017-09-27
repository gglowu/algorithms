from enum import Enum
class Color(Enum):
	White = 0
	Black = 1
######################################################
class Piece(object):
	"""docstring for Piece"""
	def __init__(self, color):
		super(Piece, self).__init__()
		self.__color = color

	def getColor(self):
		return self.__color

	def flip(self):
		if self.__color == Color.Black:
			self.__color = Color.White
		else:
			self.__color = Color.Black
######################################################
class Board(object):
	"""docstring for Board"""
	def __init__(self, rows, columns):
		super(Board, self).__init__()
		self.__rows = rows
		self.__columns = columns
		self.__board = [[None for x in range(columns)] for y in range(rows)]
		self.__blackcount = 0
		self.__whitecount = 0

	def initializeBoard(self):
		pass

	def placeColor(self, row, column, color):
		if row <= 10:
			return True
		else:
			return False

	def flipSection(self, row, column):
		pass

	def getScoreForColor(self, color):
		if color == Color.Black:
			return self.__blackcount
		else:
			return self.__whitecount

	def updateScore(self, color, newpieces):
		if color == Color.White:
			self.__whitecount += newpieces
			self.__blackcount -= newpieces
		else:
			self.__blackcount += newpieces
			self.__whitecount -= newpieces
######################################################
class Player(object):
	"""docstring for Player"""
	def __init__(self, color):
		super(Player, self).__init__()
		self.__color = color

	def getScore(self):
		return Game.getInstance().getBoard().getScoreForColor(self.__color)
	
	def playPiece(self, r, c):
		return Game.getInstance().getBoard().placeColor(r, c, self.__color)

	def getColor(self):
		return self.__color
######################################################
class Game(object):
	"""docstring for Game"""
	__instance = None

	@classmethod
	def getInstance(cls):
		if cls.__instance is None:
			cls.__instance = Game()
			return cls.__instance

	def __init__(self):
		super(Game, self).__init__()
		self.__ROWS = 10
		self.__COLUMNS = 10
		self.__board = Board(self.__ROWS, self.__COLUMNS)
		self.__players = []
		self.__players.append(Player(Color.White))
		self.__players.append(Player(Color.Black))

	def getBoard(self):
		return self.__board
		


