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

	def sendMsgToUser(userto, msg):
		if isReceived() == True:
			return True
		else:
			return False

	def sendMsgToGroupChat(groupid, msg):
		if isReceived() == True:
			return True
		else:
			return False

	def setStatus(status):
		self.__userstatus = status

	def getStatus():
		return self.__userstatus

	def addContact(newuser):
		self.__contacts[newuser.getID()] = newuser

	def getRcvedAddRequest():
		return self.__receivedaddrequests

	def addRcvedAddRequest(addrequest):
		self.__receivedaddrequests[addrequest.getUserFrom().getID()] = addrequest

	def getSentAddRequest():
		return self.__sentaddrequests

	def addSentAddRequest(addrequest):
		self.__sentaddrequests[addrequest.getUserTo().getID()] = addrequest

	def removeRcvedAddRequest(addrequest):
		self.__receivedaddrequests.remove(addrequest)

	def requestAddUser(username):
		pass

	def addPrivateConversation(privatechat):
		self.__privatechats[privatechat.getID()] = privatechat

	def addGroupConversation(groupchat):
		self.__groupchats[groupchat.getID()] = groupchat

	def getID():
		return self.__id

	def getUsername():
		return self.__username

	def getFullname():
		return self.__fullname
#############################################################################
class Conversation(object):
	"""docstring for Conversation"""
	def __init__(self, id):
		super(Conversation, self).__init__()
		self.__id = id
		self.__participants = []
		self.__msgs = []

	def getMsgs():
		return self.__msgs

	def addMsgs(msg):
		self.__msgs.append(msg)

	def getID():
		return self.__id

class GroupChat(Conversation):
	"""docstring for GroupChat"""
	def __init__(self):
		super(GroupChat, self).__init__()
	
	def removeParticipant(user):
		self.__participants.remove(user)

	def addParticipant(user):
		self.__participants.add(user)

class PrivateChat(Conversation):
		"""docstring for PrivateChat"""
	def __init__(self, user1, user2):
		super(PrivateChat, self).__init__()
		self.__user1 = user1
		self.__user2 = user2

	def getOtherParticipant(primaryuser):
		pass
##############################################################################
class Message(object):
	"""docstring for Message"""
	def __init__(self, content, date):
		super(Message, self).__init__()
		self.__content = content
		self.__date = date

	def getContent():
		return self.__content

	def getDate():
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

	def getStatus():
		return self.__requeststatus

	def getUserFrom():
		return self.__userfrom
	
	def getUserTo():
		return self.__userto

	def getDate():
		return self.__date
#############################################################################
class UserStatus(object):
	"""docstring for UserStatus"""
	def __init__(self, userstatustype):
		super(UserStatus, self).__init__()
		self.__userstatustype = userstatustype

	def getStatusType():
		return self.__userstatustype

	def setStatusType(statustype):
		self.__userstatustype = statustype
#############################################################################

				