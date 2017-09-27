from enum import Enum
#########################################################################
class VehicleType(Enum):
	Car = 0
	Van = 1
	Bus = 2
	Lorry = 3

class Vehicle(object):
	"""docstring for Vehicle"""
	def __init__(self, regnumber, vtype):
		super(Vehicle, self).__init__()
		self.__regnumber = regnumber
		self.__vtype = vtype

	def getType(self):
		return self.__vtype

	def getRegNumber(self)
		return self.__regnumber

class Bus(Vehicle):
	"""docstring for Bus"""
	def __init__(self, regnumber):
		super(Bus, self).__init__(regnumber, VehicleType.Bus)

class Van(Vehicle):
	"""docstring for Van"""
	def __init__(self, regnumber):
		super(Van, self).__init__(regnumber, VehicleType.Van)

class Lorry(Vehicle):
	"""docstring for Lorry"""
	def __init__(self, regnumber):
		super(Lorry, self).__init__(regnumber, VehicleType.Lorry)

class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self, regnumber):
		super(Car, self).__init__(regnumber, VehicleType.Car)
#########################################################################
class ParkingTicket(object):
	"""docstring for ParkingTicket"""
	def __init__(self, entertime, regnumber):
		super(ParkingTicket, self).__init__()
		self.entertime = entertime
		self.regnumber = regnumber
		self.leavetime = ""
		self.__ispaid = False
		self.__isavailable = True

	def payTicket(self):
		self.__ispaid = True

	def isPaid(self):
		return self.__ispaid

	def isAvailable(self):
		return self.__isavailable

	def destroyTicket(self):
		self.__isavailable = False

	def setLeaveTime(self, leavetime):
		self.leavetime = leavetime
#########################################################################
class ParkPot(object):
	"""docstring for ParkPot"""
	def __init__(self, availability, floornumber, uid):
		super(ParkPot, self).__init__()
		self.__availability = availability
		self.__floornumber = floornumber
		self.__uid = uid

	def getUid(self):
		return self.__uid

	def getFloorNumber(self):
		return self.__floornumber
	
	def isAvailable(self):
		return self.__availability

	def setAvailability(isavailable):
##########################################################################
class User(object):
	"""docstring for User"""
	def __init__(self, car):
		super(User, self).__init__()
		self.__car = car

	def getCarType(self):
		return self.__car.getType()

	def getRegNumber(self):
		return self.__car.getRegNumber()

	def getParkingTicket(self, parkingticket):
		self.parkingticket = parkingticket

	def payParkingTicket(self, parkingticket):
		return self.parkingticket

	def tryToDriveInto(self):
		return self.__car

	def tryToDriveOut(self):
		return self.parkingticket
##########################################################################
class ManagingSystem(object):	
	"""docstring for ManagingSystem"""
	def __init__(self, floors, potsperfloor):
		super(ManagingSystem, self).__init__()
		self.__floors = floors
		self.__potsperfloor = potsperfloor
		self.__potsavailable = floors * potsperfloor
		self.__flooravailable = []
		self.__parkingpots = []
		self.__availabletickets = []

		for f in range(0,floors):
			for p in range(0, potsperfloor):
					pp = ParkPot(True, f, generatePotsID())
					self.__parkingpots.append(pp)
			self.__flooravailable.append(potsperfloor)

	def generatePotsID(self):
		pass

	def generateEnterTime(self):
		pass

	def generateLeaveTime(self):
		pass

	def generateParkingTicket(self, regnumber):
		return ParkingTicket(generateEnterTime(), regnumber)

	def leverUp(self):
		pass

	def leverDown(self):
		pass

	def addTicket(self, parkingticket):
		self.__availabletickets.append(parkingticket)

	def removeTicket(self, parkingticket):
		pt = next(x for x in self.__availabletickets if x.regnumber == parkingticket.regnumber)
		pt.destroyTicket()
		self.__availabletickets.remove(pt)

	def payTicket(self, parkingticket):
		pt = next(x for x in self.__availabletickets if x.regnumber == parkingticket.regnumber)
		if pt.isAvailable() == True and pt.isPaid() == False:
			pt.payTicket()
			return True
		return False

	def isAllowedIn(self, car):
		if self.__potsavailable > 0:
			if car.getType() <= VehicleType.Lorry:
				this.__potsavailable -= 1
				return True
		return False

	def isAllowedOut(self, parkingticket):
		pt = next(x for x in self.__availabletickets if x.regnumber == parkingticket.regnumber)
		if pt.isAvailable() == True and pt.isPaid() == True:
			this.__potsavailable += 1
			return True
		else:
			return False
#######################################################################


def main():
	carpark1 = ManagingSystem(4, 100)
	car1 = Car("010203")
	user1 = User(car1)

	if carpark1.isAllowedIn(user1.tryToDriveInto()) == True:
		pt = carpark1.generateParkingTicket(user1.getRegNumber())
		user1.getParkingTicket(pt)
		carpark1.addTicket(pt)
		carpark1.leverUp()
		carpark1.leverDown()
	else:
		print("can not park here")
		return

	if carpark1.payTicket(user1.payParkingTicket()) == True:
		pass
	else:
		print("Failed to pay ticket")

	if carpark1.isAllowedOut(use1.tryToDriveOut()) == True:
		carpark1.removeTicket(use1.tryToDriveOut())
		carpark1.leverUp()
		carpark1.leverDown()
	else:
		print("can not drive out")
		return 
#######################################################################

if __name__ == "__main__":
    main()

		
		
		