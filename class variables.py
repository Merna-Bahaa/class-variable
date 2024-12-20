
"""
Created on Tue Nov 14 20:10:52 2023

@author: ascom
"""

"""
Class or Static Variables

> a static variable is a variable that is shared among all instances of a class, 
    rather than being unique to each instance.
    
> Static variables are defined inside the class definition, but outside of any method definitions. 

> They are typically initialized with a value, just like an instance variable, 
  but they can be accessed and modified through the class itself, rather than through an instance.    
"""



# Python program to show that the variables with a value 
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll		 


a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name)
print(a.roll)
print(b.roll) 
print(CSStudent.stream) 
CSStudent.stream = 'mech'

print(a.stream) 
print(b.stream) 
 












