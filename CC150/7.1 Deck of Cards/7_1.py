from enum import Enum, unique
#####################################
@unique
class Suit(Enum):
	Club = 0
	Diamond = 1
	Heart = 2
	Spade = 3

	"""docstring for Suit"""
	def __init__(self, value):
		super(Suit, self).__init__()
		self.__value = value

	def getValue():
		return self.__value;

	def getSuitFromValue(value):
		pass
#####################################
class Card(objec):
	"""docstring for Suit"""
	def __init__(self, c, s):
		super(Suit, self).__init__()
		self.__available = True
		self._facevalue = c
		self._suit = s
		self._facevalue = 0

	def suit():
		return self._suit

	def isAvailable():
		return self.__available

	def setAvailability(setting):
		self.__available = setting
#####################################
class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.__cards = []
		self.dealtindex = 0

	def setDeckOfCards(cards):
		self.__cards = cards
	def shuffle():
		pass
	def remaingCards():
		return len(self.__cards) - dealtindex
	def dealHand(number):
		pass
	def dealCard():
		pass
#####################################
class Hand(object):
	"""docstring for Hand"""
	def __init__(self):
		super(Hand, self).__init__()
		self.__cards = []

	def score():
		sum = 0
		for card in self.__cards:
			sum += card.value()

		return sum

	def addCard(card):
		self.__cards.append(card)
#####################################
class BlackJackCard(Card):
	"""docstring for BlackJackCard"""
	def __init__(self):
		super(BlackJackCard, self).__init__()

	def value():
		if isAce() == True:
			return 1
		elif self._facevalue >= 11 and self._facevalue <= 13
			return 10
		else:
			return self._facevalue

	def minValue():
		if isAce() == True:
			return 1
		else:
			return value()

	def maxValue():
		if isAce() == True:
			return 11
		else:
			return value()
	
	def isAce():
		return self._facevalue == 1

	def isFaceCard():
		return self._facevalue >= 11 and self._facevalue <= 13
#####################################
class BlackJackHand(Hand):
	"""docstring for BlackJackHand"""
	def __init__(self):
		super(BlackJackHand, self).__init__()

	def isBlackJack():
		pass

	def is21():
		pass

	def isFished():
		pass
