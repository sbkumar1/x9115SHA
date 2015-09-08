#!/usr/bin/python -b

class employee:
	
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __repr__(self):
		return 'Employee Name=%s, Age=%s' % (self.name, self.age)
	def __lt__(self,other):
		if (self.age>other.age):
			return True
		else:
			return False

ep1=employee('Shashank',16)
ep2=employee('shank',0)

print ep1
print ep1.__lt__(ep2)

