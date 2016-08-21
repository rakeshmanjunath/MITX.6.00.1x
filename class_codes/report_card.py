
from class_grades import *

def GradeSheet(course):
	"""course of type Grades"""
	report = ''
	
	for s in course.allStudents():
		tot=0.0
		numGrades=0.0
		
		for g in course.getGrades(s):
			tot += g
			numGrades += 1
			
		try:
			average = tot/numGrades
			report = report+ '\n' \
			         + str(s) + '\'s mean grade is ' \
					 + str(average)
		except:
			report = report+ '\n' \
		             + str(s) + ' has no grades'

	return report

stu1 = student('John Doe')
stu2 = student('John Doe')
stu3 = student('Billy Bucker')
stu4 = student('Bucky F. Dent')
stu5 = student('David Henry')

sixhundred = Grades()
sixhundred.addStudent(stu1)
sixhundred.addStudent(stu2)
sixhundred.addStudent(stu3)
sixhundred.addStudent(stu4)

for s in sixhundred.allStudents():
	sixhundred.addGrade(s,75)

sixhundred.addGrade(stu1,45)
sixhundred.addGrade(stu2,100)
sixhundred.addGrade(stu3,90)
sixhundred.addGrade(stu4,60)

sixhundred.addStudent(stu5)

print GradeSheet(sixhundred)


