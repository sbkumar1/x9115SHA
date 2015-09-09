################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###Homework 2 - Exercise 3.1####################################
################################################################

#Commenting this to make the other programs run!
"""
#!/usr/bin/python -b

repeat_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
#repeat_lyrics()

"""

################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###Homework 2 - Exercise 3.2####################################
################################################################

#!/usr/bin/python
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."
print "********************Homework 2 Exercise 3.2************************"
repeat_lyrics()
print "*******************************************************************"
print 
print

"""
Output :- 
root@ubuntu:~/CSC791/Code2# python exercise3.2.py 
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
root@ubuntu:~/CSC791/Code2# 

This is because when repeat_lyrics is called, it has both print_lyrics and repeat_lyrics defined.
"""
################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.3##########################################
################################################################



def right_justify(user):
	lengthOfUser=len(user)
	remainingLength=71-lengthOfUser
	sentence=' '*remainingLength+user
	print sentence
	#print sentence[-1]
	#print sentence.index(sentence[-1])
print "********************Homework 2 Exercise 3.3*********************"
right_justify('allen')
print "****************************************************************"
print 
print 
"""
OUTPUT:
root@ubuntu:~/CSC791/Code2# python  exercise3.3.py 
                                                                  allen
"""

##########################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.4##########################################
################################################################



def do_twice(f):
	f()
	f()

def print_spam():
	print "spam"

print "*******Calling do_twice in step 1 of exercise 3.4****"
do_twice(print_spam)
print "***************************************************************"
print 
print

def modified_do_twice(f,v):
        f(v)
        f(v)
def print_spam1(v):
	print v
print "**********Calling modified do_twice in step 2 of exercise 3.4*****"
modified_do_twice(print_spam1,'spam')
print "******************************************************************"
print
print

def print_twice(string_twice):
	print string_twice
	print string_twice
print "***********Calling print_twice in step 3 of exercise 3.4********" 
print_twice("print_twice called")
print 
print 

def modified_do_twice(f,v):
        f(v)
        f(v)
print "**********Calling modified do_twice in step 4 of exercise 3.4*****"
modified_do_twice(print_twice,'spam')
print "******************************************************************"
print
print

print "**********Calling do_four as asked in step 5 of exercise 3.5******"
def do_four(f,v):
	for i in range(4):
		f(v)
do_four(print_twice,'spam')
print "******************************************************************"
print
print

#############################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.5##########################################
################################################################


def print_figure(row,column):
	for i in range(row+1):
		for j in range(column+1):
			if ((i%5==0) and (j%5==0)):
				print "+",
			elif (i%5==0):
				print "-",
			elif (j%5==0):
				print "|",
			else:
				print " ",
			j=j+1
		print 
		i=i+1
print "Printing Part 1 of the exercise 3.5" 
print_figure(10,10)

print "Printing Part 2 of the exercise 3.5"
#print_figure(15,15)
print_figure(20,20)


      
#############################################################################
