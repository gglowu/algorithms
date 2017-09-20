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

	def getID():
		return self.__ID

	def getName():
		return self.__name

	def setName(bookname):
		self.__name = bookname

	def getAuthor():
		return self.__author

	def setAuthor(authorname):
		self.__author = authorname

	def getLanguage():
		return self.__language

	def setLanguage(booklanguage):
		self.__language = booklanguage

	def getPageCount():
		return self.__pagecount

	def setPageCount(pagecount):
		self.__pagecount = pagecount

	def getCurrentPage():
		return self.__currentpage

	def setCurrentPage(currentpage):
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

	def getCrtDisplayer():
		return self.__crtdisplayer

	def setCrtDisplayer(displayer):
		self.__crtdisplayer = displayer

	def getCrtBook():
		return self.__crtdisplayer.getCurrentBook()

	def setCrtBook(book):
		self.__crtdisplayer.setCurrentBook(book)

	def getUsrName():
		return self.__usrname

	def getUsrPwd():
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

	def getBooksAmount():
		return self.__booksamount

	def searchByID(bookid):
		book = next(x for x in self.__booklist if x.__ID == bookid)
		return book

	def searchByName(bookname):
		book = next(x for x in self.__booklist if x.__name == bookname)
		return book

	def addBook(book):
		self.__booklist.append(book)
		self.__booksamount += 1

	def deleteBook(book):
		self.__booklist.remove(book)
		self.__booksamount -= 1
######################################################################
class Displayer(object):
	"""docstring for Displayer"""
	def __init__(self, usr):
		super(Displayer, self).__init__()
		self.__usr = usr
		self.__currentbook = None


	def getCurrentBook():
		return self.__currentbook

	def setCurrentBook(book):
		self.__currentbook = book

	def displayBook(book):
		pass

	def displayCrtBook():
		displayBOok(self.__currentbook)

	def jumpToPage(book, pagegoto):
		pass

	def closeBook(book):
		pass

	def changeFontSize():
		pass

	def changeBKGroundColor():
		pass

	def nextPage(book, crtpage):
		pass

	def prePage(book, crtpage):
		pass
############################################################################
class UsrManager(object):
	"""docstring for UsrManager"""
	def __init__(self):
		super(UsrManager, self).__init__()
		self.__usrlist = []

	def generateUsrID():
		pass

	def addUsr(usrname, usrpwd, usrid):
		newusr = User(generateUsrID(), usrname, usrpwd)
		self.__usrlist.append(newusr)

	def deleteUsr(usr):
		self.__usrlist.remove(usr)

	def isUsrnameAvailable(usrname):
		return True

	def isUsrpwdAvailable(usrpwd):
		return True
	
	def login(usrname, usrpwd):
		usr = next(x for x in self.__usrlist if x.getName() == usrname)
		return usr.getUsrPwd() == usrpwd

	def changeUsrpwd(usrname, oldpwd, newpwd):
		pass
############################################################################
class OnlineReaderSystem(object):
	"""docstring for OnlineReaderSystem"""
	def __init__(self):
		super(OnlineReaderSystem, self).__init__()
		self.__activeUsr = []
		self.__usrmanager = UsrManager()
		self.__library = Library(libraryid)

	def login(user):
		if self.__usrmanager.login(user.getName(), user.getUsrPwd()) == True:
			self.__activeUsr.append(user)
			return True
		else:
			return False

	def readCrtBook(user):
		user.getCrtDisplayer().displayCrtBook()

	def readBook(user, book):
		user.getCrtDisplayer().readBook(book)

	def closeBook(user. book):
		user.getCrtDisplayer().closeBook(book)

	def nextPage(user):
		user.getCrtDisplayer().nextPage()

	def prePage(user):
		user.getCrtDisplayer().prePage()



		
		