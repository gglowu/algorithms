from enum import Enum

class User(object):
	"""docstring for User"""
	def __init__(self, id, username):
		super(User, self).__init__()
		self.__id = id
		self.__username = username
		self.__fullname = ""
		self.__userstatus = None
		self.__privatechats = {}
		self.__groupchats = {}
		self.__receivedaddrequests = {}
		self.__sentaddrequests = {}
		self.__contacts = {}

	def sendMsgToUser(self, userto, msg):
		if isReceived() == True:
			return True
		else:
			return False

	def sendMsgToGroupChat(self, groupid, msg):
		if isReceived() == True:
			return True
		else:
			return False

	def setStatus(self, status):
		self.__userstatus = status

	def getStatus(self):
		return self.__userstatus

	def addContact(self, newuser):
		self.__contacts[newuser.getID()] = newuser

	def getRcvedAddRequest(self):
		return self.__receivedaddrequests

	def addRcvedAddRequest(self, addrequest):
		self.__receivedaddrequests[addrequest.getUserFrom().getID()] = addrequest

	def getSentAddRequest(self):
		return self.__sentaddrequests

	def addSentAddRequest(self, addrequest):
		self.__sentaddrequests[addrequest.getUserTo().getID()] = addrequest

	def removeRcvedAddRequest(self, addrequest):
		self.__receivedaddrequests.remove(addrequest)

	def requestAddUser(self, username):
		pass

	def addPrivateConversation(self, privatechat):
		self.__privatechats[privatechat.getID()] = privatechat

	def addGroupConversation(self, groupchat):
		self.__groupchats[groupchat.getID()] = groupchat

	def getID(self):
		return self.__id

	def getUsername(self):
		return self.__username

	def getFullname(self):
		return self.__fullname
#############################################################################
class Conversation(object):
	"""docstring for Conversation"""
	def __init__(self, id):
		super(Conversation, self).__init__()
		self.__id = id
		self.__participants = []
		self.__msgs = []

	def getMsgs(self):
		return self.__msgs

	def addMsgs(self, msg):
		self.__msgs.append(msg)

	def getID(self):
		return self.__id

class GroupChat(Conversation):
	"""docstring for GroupChat"""
	def __init__(self):
		super(GroupChat, self).__init__()
	
	def removeParticipant(self, user):
		self.__participants.remove(user)

	def addParticipant(self, user):
		self.__participants.add(user)

class PrivateChat(Conversation):
		"""docstring for PrivateChat"""
	def __init__(self, user1, user2):
		super(PrivateChat, self).__init__()
		self.__user1 = user1
		self.__user2 = user2

	def getOtherParticipant(self, primaryuser):
		pass
##############################################################################
class Message(object):
	"""docstring for Message"""
	def __init__(self, content, date):
		super(Message, self).__init__()
		self.__content = content
		self.__date = date

	def getContent(self):
		return self.__content

	def getDate(self):
		return self.__date
#############################################################################
class UserStatusType(Enum):
	"""docstring for UserStatusType"""
	Offline = 0
	Away = 1
	Available = 2
	Busy = 3
#############################################################################
class RequestStatus(Enum):
	Unread = 0
	Read = 1
	Accepted = 2
	Rejected = 3
#############################################################################
class AddRequest(object):
	"""docstring for AddRequest"""
	def __init__(self, userfrom, userto, date):
		super(AddRequest, self).__init__()
		self.__userfrom = userfrom
		self.__userto = userto
		self.__date = date
		self.__requeststatus = None

	def getStatus(self):
		return self.__requeststatus

	def getUserFrom(self):
		return self.__userfrom
	
	def getUserTo(self):
		return self.__userto

	def getDate(self):
		return self.__date
#############################################################################
class UserStatus(object):
	"""docstring for UserStatus"""
	def __init__(self, userstatustype):
		super(UserStatus, self).__init__()
		self.__userstatustype = userstatustype

	def getStatusType(self):
		return self.__userstatustype

	def setStatusType(self, statustype):
		self.__userstatustype = statustype
#############################################################################

				