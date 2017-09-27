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

	def getValue(self):
		return self.__value;

	def getSuitFromValue(self,value):
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

	def suit(self):
		return self._suit

	def isAvailable(self):
		return self.__available

	def setAvailability(self,setting):
		self.__available = setting
#####################################
class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.__cards = []
		self.dealtindex = 0

	def setDeckOfCards(self,cards):
		self.__cards = cards
	def shuffle(self):
		pass
	def remaingCards(self):
		return len(self.__cards) - dealtindex
	def dealHand(self,number):
		pass
	def dealCard(self):
		pass
#####################################
class Hand(object):
	"""docstring for Hand"""
	def __init__(self):
		super(Hand, self).__init__()
		self.__cards = []

	def score(self):
		sum = 0
		for card in self.__cards:
			sum += card.value()

		return sum

	def addCard(self,card):
		self.__cards.append(card)
#####################################
class BlackJackCard(Card):
	"""docstring for BlackJackCard"""
	def __init__(self):
		super(BlackJackCard, self).__init__()

	def value(self):
		if isAce() == True:
			return 1
		elif self._facevalue >= 11 and self._facevalue <= 13
			return 10
		else:
			return self._facevalue

	def minValue(self):
		if isAce() == True:
			return 1
		else:
			return value()

	def maxValue(self):
		if isAce() == True:
			return 11
		else:
			return value()
	
	def isAce(self):
		return self._facevalue == 1

	def isFaceCard(self):
		return self._facevalue >= 11 and self._facevalue <= 13
#####################################
class BlackJackHand(Hand):
	"""docstring for BlackJackHand"""
	def __init__(self):
		super(BlackJackHand, self).__init__()

	def isBlackJack(self):
		pass

	def is21(self):
		pass

	def isFished(self):
		pass
