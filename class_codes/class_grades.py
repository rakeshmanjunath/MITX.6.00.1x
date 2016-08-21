
from class_mitperson import *

class Grades(object):
	"""A mapping from students to a list of grades"""
	
	def __init__(self):
		"""create empty grade book"""
		self.students = []
		self.grades = {}
		self.isSorted = True
		
	def addStudent(self,student):
		"""Assumes: student is of type student
		   Add student to the grade book"""
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False
	
	def addGrade(self, student, grade):
		"""Assumes: grade is a float
		   Add grade to the list of grades for student"""
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('Student not in mapping')
	
	def getGrades(self,student):
		"""Return a list of grades for student"""
		try:
			return self.grades[student.getIdNum()][:]
		except:
			raise ValueError('stident not in mapping')
		
	def allStudents(self):
		"""Return a list of the students in the grade book"""
		if not self.isSorted:
			self.students.sort()
		# return self.students[:] # return copy of list of students
		for s in self.students:
			yield s


