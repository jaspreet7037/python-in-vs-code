# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

i = int(input("ENTER YOUR CURRENT AGE : "))
st = str(input("ENTER YOUR NAME : "))
j = int(input("ENTER YOUR BIRTHDAY YEAR : "))
person1 = Person(st,i)
person2 = Person.fromBirthYear(st, j)

print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(17))
