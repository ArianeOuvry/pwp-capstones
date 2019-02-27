#----------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------USER Class-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

class User:
	def __init__(self, name, email):
		self.name=name
		self.email=email
		self.books={}    
		#books is an empty dictionnary mappping the book object to the user's rating of the book name and email are strings

	def get_email(self):
	  #returns user's email
		return self.email


	def change_email(self, address):
	  #updates email of user prints a message confirming update
		self.email=address
		message="{} 's email has been updated to {}".format(self.name,self.email)
		return message
	  
	def number_books_read(self):
	  #counts the number of books for this user
		book_count=0
		for book in self.books:
			book_count+=1
		return book_count
		
	def number_books_with_rating(self):
	#counts the number of books for this user with rating
		book_with_rating=0
		for book in self.books:
			if self.books[book]!=None:
				book_with_rating+=1
		return book_with_rating
		    
	def __repr__(self):
	  #what you get when you print a user
		return "User {name}, {email}, {count} books read".format(name=self.name,email=self.email,count=self.number_books_read())

	def __eq__(self, other_user):
	  #compares users returns true if both users have the same name and email
		if self.name==other_user.name and self.email==other_user.email:
			return True
			
	def read_book(self, book, rating=None):
		self.books[book]=rating		
		#adds a book and a rating to the self.books dictionary where book is the key and rating the value
		
	def get_average_rating(self):
		total_rating_user=0
		if User.number_books_with_rating(self)>0:
			for value in self.books.values():
				if value!=None:
					total_rating_user+=value
			average=total_rating_user/User.number_books_with_rating(self)
			return average
		else:
			return "User has read no books or has rated no books"
	
#--------------------------------------------------------------------------------------------------------------------------------------	
#---------------------------------------BOOK Class and Sub Classes------------------------------------------------------------------   
#-------------------------------------------------------------------------------------------------------------------------------------
  
class Book:
	def __init__(self, title, isbn, price=None):
		self.title=title
		self.isbn=isbn
		self.ratings=[]
		self.price=price
		#title is a string isbn is a number ratings is a list
		
	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self,new_isbn):
		#updates the book's isbn to a new isbn and prints a message to confirm update
		self.isbn=new_isbn
		message="The isbn of book {} has been updated to {}.".format(self.title,self.isbn)
		return message
		
	def add_rating(self,rating):
		#appends rating to the ratings list but rating has to be from 0 to 4
		if rating in range(5) or rating==None:
			return self.ratings.append(rating)
		else:
			return "Invalid Rating"
		
	def __eq__(self, other_book):
	  #compares books returns true if both books have the same title and isbn
	  if self.title==other_book.title and self.isbn==other_book.isbn:
		  return True
	
	def __repr__(self):
		#returns title 
		return self.title
		  
	def get_average_rating(self):
		#create a new list with the ratings not None then get the average from that
		valid_ratings=[rating for rating in self.ratings if rating!=None] 
		total_rating_book=0
		if len(valid_ratings)>0:
			for rating in valid_ratings:
				total_rating_book+=rating
			return total_rating_book/len(valid_ratings)
		else:
			return "No ratings for this book"
			
	def __hash__(self):
		return hash((self.title, self.isbn))

		  
#---------------------------------------------------------------------------------------------------------
		  
class Fiction(Book):
	def __init__(self, title, author, isbn, price=None):
		#call constructor of parent Book class and adds author variable
		super().__init__(title,isbn,price)
		self.author=author
		
	def get_author(self):
		return self.author
	
	def __repr__(self):
		#returns title by the author
		return "{title} by {author}".format(title=self.title,author=self.author)

#--------------------------------------------------------------------------------------------------------------------
		
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn, price=None):
		#call constructor of parent Book class and adds subject and level string variable
		super().__init__(title,isbn,price)
		self.subject=subject
		self.level=level
		
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
	
	def __repr__(self):
		#returns title level and subject
		return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level,subject=self.subject)
		
#---------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------TOMERATER CLASS------------------------------------------------------------------------
# for the get creative, I did what was listed and for my own ideas, I tried to adjust the methods to accomodate when users/users had the 
# same read counts or average ratings
#--------------------------------------------------------------------------------------------------------------------------------

class TomeRater:
	def __init__(self):
		self.users={}
		# dictionary which will map a user's email  KEY to the corresponding USER object VALUE
		self.books={}
		# dictionary which will map a BOOK object KEY to the number of Users that have read it VALUE

# 3 methods creating the 3 types of book class------------------------
#added 1 isbn check method that I can reference to check unique isbn in self.books
	
	def isbn_check(self,isbn):
		#checks if book in self.books dictionnary already has this isbn - function to be referenced by other tomerater methods
		check=False
		for book in self.books:
			if isbn==book.get_isbn():
				check=True
		return check
	
	def TomeRater_has_books(self):
		#checks if self.books has entries - to be referenced by other methods
		if self.books!={}:
			return True
	
	def TomeRater_has_users(self):
		#checks if self.users has entries - to be referenced by other methods
		if self.users!={}:
			return True
	
	def create_book(self, title, isbn, price=None):
		if self.isbn_check(isbn):
			print( "ISBN already exist, please adjust")
		else:
			return Book(title, isbn, price)
	
	def create_novel(self, title, author, isbn, price=None):
		if self.isbn_check(isbn):
			print( "ISBN already exist, please adjust")
		else:
			return Fiction(title, author, isbn, price)
	
	def create_non_fiction(self, title, subject, level, isbn, price=None):
		if self.isbn_check(isbn):
			print( "ISBN already exist, please adjust"	)
		else:
			return Non_Fiction(title, subject, level, isbn, price)
#-----------------------------------------------------------------------

# method checks if the user is in the mapping email to user dictionary, if this user is in it
# it adds the book and rating the the user's book dictionnary and adds the rating to the book rating list
#it then adds or update the books read count in the self.books dictionnary

	def add_book_to_user(self, book, email, rating=None):
		if email in self.users:
			self.users[email].read_book(book,rating)
			book.add_rating(rating)
			if book in self.books:
				self.books[book]+=1
			else:
				self.books[book]=1	
		else:
			print( "No user with {} email !".format(email))

	
#---------------------------------------------------------------------------					
# creates a new User object from name and email and as option a LIST of books,  then if user_books is provided it 
#should loop trough the list and add each book to the user using the tomerater 
#method add book to user
				
	def add_user(self, name, email, user_books=None):
		
		#checks if email provided is valid
		valid_extensions=['.com', '.edu', '.org']
		if email[-4:] not in valid_extensions or '@' not in email:
			print ("invalid email - please reenter")
		
		else:		
		#only adds user if user email is not already in the dictionary  
			if email not in self.users:
				new_user=User(name,email)
				self.users[new_user.email]=new_user
				print("user {} added".format(name))
				if user_books != None:
					for book in user_books:
						self.add_book_to_user(book, email)
			else:
				print("email already exist - change email please")
								

#--------------------------------------------------------------------------
#---------------------------------------quick output methods-------------------
	
	def print_catalog(self):
		for book in self.books:
			print (book)
		
	
	def print_users(self):
		for email in self.users.keys():
			print (self.users[email])
		
	
	
	def __repr__(self):
		#probably a nicer way to display this
		return "Registered Users:\n {} \n Catalogue:\n {}".format(self.users,self.books)
		
		
	def __eq__(self,other): 
		if self.users == other.users and self.books == other.books:
			return True
		else:
			return False
	
	
#---------------------------------Advanced analytics methods----------------------------------------



	def get_most_read_book(self):
		#accomodates books with the same number of read counts	- checks if there are books in self books dictionary
		if self.TomeRater_has_books():
		
			max_readings=0
			
			for value in self.books.values():
				#finds the highest count
				if value>max_readings:
					max_readings=value					
			
			for book in self.books:
				#finds the books matching this highest count and prints them followed by a sentence with the count
				if self.books[book]==max_readings:
					print(book)		
			return "with a read count of {}".format(max_readings)
		
		else:
			return "There are no books registered"
			
#-------------------------------------------------------------------------------------------------
				
	def highest_rated_book(self):
		#accomodates books with the same rating average- checks 1st if there are books in the self.books dictionary
		
		if self.TomeRater_has_books():
			
			best_rated=0
			
			for book in self.books:
				if type(book.get_average_rating())!=str:
					#checks if the book has an average rating then finds the best rating
					if book.get_average_rating()>best_rated:
						best_rated=book.get_average_rating()
			
			if best_rated==0:
				return "no books with ratings"
			
			else:
				#return all books where the average matches the best
				for book in self.books:				
					if book.get_average_rating()==best_rated:
						print(book)
				return "with an average score of {}".format(best_rated)

		else:
			return "There are no books registered"
			
#------------------------------------------------------------------------------------------------------		
	
	def most_positive_user(self):

		#accomodates users with the same rating average - checks if there are users in self.users 1st
		if self.TomeRater_has_users(): 
			
			best_average=0
			
			for user in self.users.values():
				if type(user.get_average_rating())!=str:
				#checks if the user has an average rating and determines highest average					
					if user.get_average_rating()>best_average:
						best_average=user.get_average_rating()
			
			if best_average==0:
				return "no users with book ratings"
			
			else:
				#returns users where average matches best average
				for user in self.users.values():				
					if user.get_average_rating()==best_average:
							print(user)
				return "with an average rating of {}".format(best_average)
		
		else:
			return "There are no users registered"
	
	
#------------for all n functions below - error check on n being int and >0 should probably be added----------------------------------------------------------------------------------	
			
				
	def get_n_most_read_books(self,n):		
		#creates a sorted list of pairs (read counts, book title) from self book dictionary 
		#then sorts and returns the last n from the end of the list - will be partial if many books have the same read count

			
		if self.TomeRater_has_books():
			
			book_list=[(value,key.get_title()) for key,value in self.books.items()]
			book_list.sort()
			n=min(n,len(book_list))	# so index is never out of range if list is shorter than n	
			
			index=1
			print("Here are the most {} read books:\n(returning all the books referenced if the number requested is greater than the number of books referenced)".format(n))
			while index<=n:
				print("{} with a read count of {}.".format(book_list[-index][1],book_list[-index][0]))
				index+=1
		
		else:
			return "There are no registered books"
				

	
#-----------------------------------------------------------------------------------------------------
			
		
	def get_n_most_prolific_readers(self,n):
		#creates a sorted list of pairs (read counts, email)
		#then sorts and returns the last n from the end of the list - will be partial if many readers have read the same number of books
		
		if self.TomeRater_has_users():
			
			user_list=[(value.number_books_read(),value.name) for value in self.users.values()]
			user_list.sort()
			n=min(n,len(user_list))	# so index is never out of range if list is shorter than n	
			index=1
			
			print("Here are the most {} prolific readers:\n (returning all the users referenced if the number requested is greater than the number of users referenced)".format(n))
			while index<=n:
				print( "{} with a book read count of {}.".format(user_list[-index][1],user_list[-index][0]))
				index+=1
		else:
			return "There are not registered users"
			
		
#-------------------------------------------------------------------------
	def get_n_most_expensive_books(self,n):
		#checks if there are books
		#checks if at least 1 book has a price
		#loops through the books to create a sorted list of pairs price,book
		#returns the last n from the list - will be partial if many books have the same price
		
		if self.TomeRater_has_books():		
			book_list_w_price=[(key.price,key.get_title())for key in self.books if key.price!=None]
			
			if len(book_list_w_price)==0:
				print("There are no books with prices")
			
			else:
				book_list_w_price.sort()
				n=min(n,len(book_list_w_price))	# so index is never out of range if list is shorter than n			
				index=1
				print("Here are the most {} expensive books :\n(returning all the books referenced if the number requested is greater than the number of books referenced)".format(n))
				while index<=n:
					print("{} with a price of {}.".format(book_list_w_price[-index][1],book_list_w_price[-index][0]))
					index+=1		
		else:
			return "There are no registered books"
	

#------------------------------------------------------------------------------------------

	def get_worth_of_user(self,user_email):
		#check if email exists if not return user is not referenced	
		#checks if user has read books	
		#loops through all the books read by user and sums the price
		#if no books have prices, returns message saying no prices
			
		if user_email in self.users:
			user=self.users[user_email]
			
			if user.number_books_read()>0:			
				total_cost_books=0
		
				for book in user.books:
					if book.price!=None:
						total_cost_books+=book.price			
				if total_cost_books==0:
					print("No books with prices listed for user {}".format(user.name))			
				else:			
					print ("Sum of book costs for {} is {}.".format(user.name,total_cost_books))
						
			else:
					print("User {} has read no books.".format(user.name))
				
		else:
			print( "No user with {} email !".format(email))
