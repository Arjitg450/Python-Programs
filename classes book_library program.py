
class Library:
	def __init__(self,listOfBooks):
		self.AvailableBooks = listOfBooks

	def displayAvailableBooks(self):
		for book in self.AvailableBooks:
			print(book)

	def lendbook(self,RequestedBook):
		if RequestedBook in self.AvailableBooks:
			print("you have now borrowed the book")
			self.AvailableBooks.remove(RequestedBook)
		else: 
			print("book is not available")
                       

	def addbook(self,returnnedbook):
	     
		self.AvailableBooks.append(returnedbook)
		print("thank you for retuning the book")

class Customer:
	
	def requestbook(self):
		print("enter the name of the book you want")
		self.book=input()
		return self.book
		print()
	def returnbook(self):
		print()
		print("Enter the name of the book you want to return: ")
		self.book=input()
		return self.book
		print()

library=Library(["Hellen keller","Magic of Life","path to success"])
customer=Customer()
while True:
	print("1 for Displaying the book")
	print("2 for requesting the book")
	print("3 for returning the book")
	print("4 for exit")

	userchoice= int(input())
	if userchoice==1:
	     library.displayAvailableBooks()
	elif userchoice==2:
	     RequestedBook = customer.requestbook()
	     library.lendbook(RequestedBook)
	elif userchoice==3:
	     returnedbook = customer.returnbook()
	     library.addbook(returnedbook)
	elif userchoice==4:
	     exit()











