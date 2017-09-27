class PhoneTicket(object):
	"""docstring for PhoneTicket"""
	def __init__(self, ticketid):
		super(PhoneTicket, self).__init__()
		self.ticketid = ticketid
		self.__sorted = False

	def isSorted(self):
		return self.__sorted

	def setSorted(self, isdone):
		self.__sorted = isdone
#########################################################
class Employee(object):
	"""docstring for Employee"""
	def __init__(self, employeeid):
		super(Employee, self, employeeid).__init__()
		self.employeeid = employeeid
		self.availability = True

	def isAvailable(self)
		return self.availability

	def setAvailable(self, isavailable):
		self.availability = isavailable

	def handlePhone(self, phoneticket):
		if phoneticket >= 10:
			return False
		else:
			return True

	def raiseProblem(self):
		pass
#########################################################
class Respond(Employee):
	"""docstring for Respond"""
	def __init__(self):
		super(Respond, self).__init__()
#########################################################
class Manager(object):
	"""docstring for Manager"""
	def __init__(self):
		super(Manager, self).__init__()
#########################################################
class Director(object):
	"""docstring for Director"""
	def __init__(self):
		super(Director, self).__init__()
#########################################################
class CallCenter(object):
	"""docstring for CallCenter"""
	def __init__(self):
		super(CallCenter, self).__init__()
		self.__responds = []
		self.__managers = []
		self.__directors = []

	def InitSystem(self, repondlist, managerlist, directorlist):
		self.__responds.extend(repondlist)
		self.__directors.extend(directorlist)
		self.__managers.extend(managerlist)

	def HandlePhoneCall(self, phone):
		pt = PhoneTicket(phone)

		for respond in self.__responds:
			if respond.isAvailable() == True:
				respond.setAvailable(False)
				if respond.handlePhone(pt) == True:
					pt.setSorted(True)
				else:
					respond.raiseProblem()
				respond.setAvailable(True)
				break

		if pt.isSorted == True:
			return True

		for manager in self.__managers:
			if manager.isAvailable() == True:
				manager.setAvailable(False)
				if manager.handlePhone(pt) == True:
					pt.setSorted(True)
				else:
					manager.raiseProblem()
				manager.setAvailable(True)
				break

		if pt.isSorted == True:
			return True

		for director in self.__directors:
			if director.isAvailable() == True:
				director.setAvailable(False)
				if director.handlePhone(pt) == True:
					pt.setSorted(True)
				else:
					director.raiseProblem()
				director.setAvailable(True)
				break
		
		if pt.isSorted == True:
			return True
		else:
			return False

	def WaitingForCall(self)
		while True:
			time.sleep(1000)
			id = random.randint(0, 10000000)
			HandlePhoneCall(id)