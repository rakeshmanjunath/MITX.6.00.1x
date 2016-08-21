
import datetime

class Person(object):
	def __init__(self,name):
		"""create a person with name"""
		self.name=name
		try:
			lastBlank     = name.rindex(' ')
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthday = None
	
	def getLastName(self):
		"""return self's last name"""
		return self.lastName
	
	def setBirthday(self,birthDate):
		"""Assumes birthdate is of type datetime.date
		   sets self's birthday to birthDate"""
		self.birthday=birthDate
	
	def getAge(self):
		"""returns self's current age in days"""
		if self.birthday == None:
			return ValueError
		return (datetime.date.today()-self.birthday).days
	
	def __lt__(self,other):
		"""returns True if self's name is lexographically
		   less that other's name, and False otherwise"""
		if self.lastName == other.lastName:
			return self.name<other.name
		return self.lastName<other.lastName
		
	def __str__(self):
		"""return self's name"""
		return self.name
	
