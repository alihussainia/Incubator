#-----------------------------
# --- CREATING INTERACTION ---
#-----------------------------
#COMMENTS
#Purpose: Has no impact on the program. Make the code more readable.
# try this comment
#This is a short comment

"""
This is very
very long
comment on 3 lines
"""

#DISPLAY
print("Hello, Finance!")

#-----------------------------
# --- VARIABLES ---
#-----------------------------
# Purpose: Store and manipulate data. Different types exist.

#NUMBERS
#Store and manipulate numbers.
a = 20 #Type: integer
print(a)
print ("a has value equal to ", a)
a = 20.5  #Type: float
print ("a has value equal to = " + str(a))

#Casting : Change a type to another.
a = str(20)    # a will be a string: “20”
b = int(20)    # b will be an integer: 20
c = float(20)  # c will be a float: 20.0

#STRING (OF CHARACTERS)
#Manipulate text
a = "Hello Finance"	#Type: String
print(a)

#Useful fonctions
# Indicate whether a text is included in other text
a = "The stock market is filled with individuals who know the price of everything, but the value of nothing."
if "value" in a:
  print("Yes, 'value' is there.")

# Print a new line
a = "This is the first line, \n and here the second one."
print(a)

# Replace one character or a string with another in text.
a = "Hello, Finance!"
print(a.replace("Finance", "Markets"))

#DATES
#Manipulate Dates
#https://docs.python.org/fr/3/library/datetime.html
import datetime
Today = datetime.datetime.now()
otherDate = datetime.datetime(2020, 12, 15)
#Give the month
print(Today.strftime("%b"))
#Number of the week in the year
print(otherDate.strftime("%W"))

#BOOLEAN
#Variable which can only take the values true and false. Purpose: manipulates elements of logic.
a = True  #Type: boolean
b = False
print(b)

#-----------------------------
# --- MAKING DECISIONS ---
#-----------------------------
#IF STATEMENT
#Purpose: if such a variable has such a value then do that if not do that.
a = 10
b = 5
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#WHILE LOOP
#Purpose: The while loop allows to repeat a series of instructions
# while a given condition is true, until the exit (Break) condition is true.
i = 0
while i < 5:
  print(i)
  if i == 4:
    break
  i = i + 1

#FOR LOOP
#Purpose: The for loop is used to iterate over the elements of a sequence (list, string, etc.)
# according to their order in the sequence. The exit condition in this loop is implicit:
# we will exit the loop after going through the last element of the sequence, until the exit (Break) condition is true.
for i in range(5):
  print(i)
  if i == 3:
    break

#-----------------------------
# --- RE-USING CODE ---
#-----------------------------
#LIBRAIRIES AND MODULES
#Purpose: Python is supplemented by a large number of built-in functions. These functions are saved in files called modules.
#To use them, they must be imported at the start of the program.
# import the library random
import random
# display a random number between 1 and 100
print(random.randrange(1, 100))

#FUNCTIONS
#Purpose: a function is a block of instructions intended to perform an operation.
# It can receive parameters and return a value.
#Its advantage is to create a "subroutine" for performing repetitive operations.
# Instead of writing the complete code as many times as necessary, we create a function that we will call to execute it,
# which can make the code more readable.

# Create the function
def sayHello():
  print("Hello !")
# Call the function
sayHello()

# Create the function with Argument and return
def multiplyby3(x):
    return 3 * x
# Call the function
print(multiplyby3(5))

#-----------------------------
# --- DATA STRUCTURE  ---
#-----------------------------
#Data structures are specific ways of organizing and storing data so that it can be viewed and worked on effectively.

#LIST
#A list is an ordered set of data that can be changed.
a = ["EUR", "USD", "HKD"]
print(a)
# display the first item
print(a[0])
# modify the 2nd item
a[1]="CHF"
# Insert "CAD" as the 2nd item
a.insert(1,"CAD")
# Insert "CAD" as the last item
a.append("CAD")
#Number of items
len(a)
#Test if an item is inside
if "HKD" in a:
  print("HKD is inside!")

# remove by item
a.remove("EUR")
# equivalent to the remove by index:
a.pop(0)
#remove all content
a.clear()



















