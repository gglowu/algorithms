from enum import Enum

class Language(Enum):
	English = 0
	Chinese = 1
	Germany = 2
############################################
class Book(object):			
	"""docstring for Book"""
	def __init__(self, ID):
		super(Book, self).__init__()
		self.__ID = ID
		self.__name = ""
		self.__author = ""
		self.__language = Language.Chinese
		self.__pagecount = 0
		self.__currentpage = 0

	def getID(self):
		return self.__ID

	def getName(self):
		return self.__name

	def setName(self, bookname):
		self.__name = bookname

	def getAuthor(self):
		return self.__author

	def setAuthor(self, authorname):
		self.__author = authorname

	def getLanguage(self):
		return self.__language

	def setLanguage(self, booklanguage):
		self.__language = booklanguage

	def getPageCount(self):
		return self.__pagecount

	def setPageCount(self, pagecount):
		self.__pagecount = pagecount

	def getCurrentPage(self):
		return self.__currentpage

	def setCurrentPage(self, currentpage):
		self.__currentpage = currentpage
##########################################################
class User(object):
	"""docstring for User"""
	def __init__(self, usrid, usrname, usrpwd):
		super(User, self).__init__()
		self.__usrid = usrid
		self.__usrname = usrname
		self.__usrpwd = usrpwd
		self.__crtdisplayer = None

	def getCrtDisplayer(self):
		return self.__crtdisplayer

	def setCrtDisplayer(self, displayer):
		self.__crtdisplayer = displayer

	def getCrtBook(self):
		return self.__crtdisplayer.getCurrentBook()

	def setCrtBook(self, book):
		self.__crtdisplayer.setCurrentBook(book)

	def getUsrName(self):
		return self.__usrname

	def getUsrPwd(self):
		return self.__usrpwd
#############################################################
class Library(object):
	"""docstring for Library"""
	def __init__(self, libraryid):
		super(Library, self).__init__()
		self.__libraryid = libraryid
		self.__libraryname = ""
		self.__booklist = []
		self.__booksamount = 0

	def getBooksAmount(self):
		return self.__booksamount

	def searchByID(self, bookid):
		book = next(x for x in self.__booklist if x.__ID == bookid)
		return book

	def searchByName(self, bookname):
		book = next(x for x in self.__booklist if x.__name == bookname)
		return book

	def addBook(self, book):
		self.__booklist.append(book)
		self.__booksamount += 1

	def deleteBook(self, book):
		self.__booklist.remove(book)
		self.__booksamount -= 1
######################################################################
class Displayer(object):
	"""docstring for Displayer"""
	def __init__(self, usr):
		super(Displayer, self).__init__()
		self.__usr = usr
		self.__currentbook = None


	def getCurrentBook(self):
		return self.__currentbook

	def setCurrentBook(self, book):
		self.__currentbook = book

	def displayBook(self, book):
		pass

	def displayCrtBook(self):
		displayBOok(self.__currentbook)

	def jumpToPage(self, book, pagegoto):
		pass

	def closeBook(self, book):
		pass

	def changeFontSize(self):
		pass

	def changeBKGroundColor(self):
		pass

	def nextPage(self, book, crtpage):
		pass

	def prePage(self, book, crtpage):
		pass
############################################################################
class UsrManager(object):
	"""docstring for UsrManager"""
	def __init__(self):
		super(UsrManager, self).__init__()
		self.__usrlist = []

	def generateUsrID(self):
		pass

	def addUsr(self, usrname, usrpwd, usrid):
		newusr = User(generateUsrID(), usrname, usrpwd)
		self.__usrlist.append(newusr)

	def deleteUsr(self, usr):
		self.__usrlist.remove(usr)

	def isUsrnameAvailable(self, usrname):
		return True

	def isUsrpwdAvailable(self, usrpwd):
		return True
	
	def login(self, usrname, usrpwd):
		usr = next(x for x in self.__usrlist if x.getName() == usrname)
		return usr.getUsrPwd() == usrpwd

	def changeUsrpwd(self, usrname, oldpwd, newpwd):
		pass
############################################################################
class OnlineReaderSystem(object):
	"""docstring for OnlineReaderSystem"""
	def __init__(self):
		super(OnlineReaderSystem, self).__init__()
		self.__activeUsr = []
		self.__usrmanager = UsrManager()
		self.__library = Library(libraryid)

	def login(self, user):
		if self.__usrmanager.login(user.getName(), user.getUsrPwd()) == True:
			self.__activeUsr.append(user)
			return True
		else:
			return False

	def readCrtBook(self, user):
		user.getCrtDisplayer().displayCrtBook()

	def readBook(self, user, book):
		user.getCrtDisplayer().readBook(book)

	def closeBook(self, user. book):
		user.getCrtDisplayer().closeBook(book)

	def nextPage(self, user):
		user.getCrtDisplayer().nextPage()

	def prePage(self, user):
		user.getCrtDisplayer().prePage()



		
		