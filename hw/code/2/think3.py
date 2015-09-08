################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###Homework 2 - Exercise 3.1####################################
################################################################


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
OUTPUT:-
root@ubuntu:~/CSC791/Code2# python exercise3.1.py 
Traceback (most recent call last):
  File "exercise3.1.py", line 3, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
root@ubuntu:~/CSC791/Code2#

repeat_lyrics is called before function definition 
"""
################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###Homework 2 - Exercise 3.2####################################
################################################################

#!/usr/bin/python -b
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."
repeat_lyrics()

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

#!/usr/bin/python -b


def right_justify(user):
	lengthOfUser=len(user)
	remainingLength=71-lengthOfUser
	sentence=' '*remainingLength+user
	print sentence
	#print sentence[-1]
	#print sentence.index(sentence[-1])
right_justify('allen')

"""
OUTPUT:
root@ubuntu:~/CSC791/Code2# python  exercise3.3.py 
                                                                  allen
"""
################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.4.1##########################################
################################################################

#!/usr/bin/python -b

def do_twice(f):
        f()
        f()

def print_spam():
        print "Spam"
do_twice(print_spam)

##########################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.4##########################################
################################################################

#!/usr/bin/python -b

def do_twice(f,v):
        f(v)
        f(v)

def print_spam(num):
        print "Spam"

print "***********EXERCISE  3.4 STEP 2"
do_twice(print_spam,2)

def print_twice(string_twice):
        print string_twice
        print string_twice

def modified_do_twice(f,v):
        f(v)
        f(v)
print "************* EXERCISE 3.4 STEP 3******************"
print_twice("printing twice")
print
print

print "EXERCISE 3.4 STEP 4"
modified_do_twice(print_twice,'spam')
print
print

print "EXERCISE 3.4 STEP 5"
def do_four(f,v):
        for i in range(4):
                f(v)
do_four(print_twice,'spam')


"""
OUTPUT:-
root@ubuntu:~/CSC791/Code2# python exercise3.4.py 
Calling modified do twice in step 2 of exercise 3.4
HelloHello
HelloHello
Calling modified do_twice in step 4 of exercise 3.4
spamspam
spamspam
Calling do_four as asked in step 5 of exercise 3.5
do_twicedo_twice
do_twicedo_twice
do_twicedo_twice
do_twicedo_twice
root@ubuntu:~/CSC791/Code2# 
"""
#############################################################################

################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###HW 2 - Exercise 3.5##########################################
################################################################
#!/usr/bin/python -b

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
print_figure(15,15)
print_figure(20,20)

"""
OUTPUT:-
root@ubuntu:~/CSC791/Code2# python exercise3.5.py 
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
|         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - +
root@ubuntu:~/CSC791/Code2# 
"""
#############################################################################
