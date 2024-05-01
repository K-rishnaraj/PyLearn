# -*- coding: utf-8 -*-
"""PythonLearn101.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/***
"""

print("This")

x = 1
if x == 1:
 print(" x is " ,x, " since its true ")

"""Numbers"""

#integer
myint = 7
print(myint)

#float
myfloat = 7.0
print(myfloat)
myfloat = 7
print(myfloat)
myfloat = float(myfloat)
print(myfloat)

"""Strings"""

mystring = 'hello'
print(mystring)
mystring = "hello"
print (mystring)

#double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print (three)

hello = "hello"
world = "world"
helloworld = hello + " ;) " +world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously"
a, b = 3, 4
print(a, b)

#Mixing operators between numbers and strings is not supported:
one = 1
two = 2
hello ="hello"
#print (one+ two + hello)
print (one ,two , hello)

"""**Exercise**
The target of this exercise is to create a string, an integer, and a floating point number.
The string should be named mystring and should contain the word "hello".
The floating point number should be named myfloat and should contain the number 10.0, and
 the integer should be named myint and should contain the number 20.
"""

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

"""List"""

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print ( mylist[0])
print ( mylist[1])
print ( mylist[2])

for x in mylist:
  print(x)

mylist = [1,2,3]
print(mylist[10]) #Error list

"""**Exercise**
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
"""

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

"""**Arithmetic Operators**"""

number = 1 + 2 * 3 / 4.0
print(number)

#modulo (%) operator. eturns the integer remainder of the division. dividend % divisor = remainder
remainder = 11 % 3
print(remainder)

#two multiplication symbols makes a power relationship.
#Power operator
squared = 7 ** 2 # 7^2
cubed = 2 ** 3  #2^3
print(squared)
print(cubed)

"""Using Operators with **Strings**"""

helloworld = "hello" + " " + "world"
print(helloworld)

#Python also supports multiplying strings to form a string with a repeating sequence:

lotsofhellos = "hello" * 10
print(lotsofhellos)

"""**Using Operators with Lists**"""

#Lists can be *joined* with the addition operators:
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:

print([1,2,3] * 3)

"""**Exercise**
The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.


"""

x = object()
y = object()

# TODO: change this code




x_list = [x] * 10




y_list = [y] * 10



big_list = x_list + y_list




print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))


# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

"""**String Formatting**
Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
"""

name = "John"
print("Hello,%s!" %name)

#To use two or more argument specifiers, use a tuple (parentheses):

name = "John"
age = 23
print("%s is %d years old."%(name,age))

"""To use two or more argument specifiers, use a tuple (parentheses):"""

mylist = [1,2,3]
print("A list: %s" % mylist)

"""**%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)**

**Exercise
You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.**
"""

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

"""**Basic String Operations**"""

string = "Hello world"
print ("single quotes are'' ")
print(len(string))

string = "Hello world"
print(string.index("o"))

"""That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.

To make things more simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.
"""

string = "Hello world"
print(string.count("l"))

string = "Hello world!"
print (string[3:7])

"""This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.

If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.

You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end".
"""

string = "Hello world"
print(string[3:7:2])

"""This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step]."""

string = "Hello world!"
print(string[3:7])
print(string[3:7:1])

"""There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this"""

string = "Hello world!"
print(string[::-1])

string = "Hello world!"
print(string.upper())
print(string.lower())

"""These make a new string with all letters converted to uppercase and lowercase, respectively."""

string = "Hello world!"
print(string.startswith("Hello"))
print(string.endswith("asdfasdfasdf"))

"""This is used to determine whether the string starts with something or ends with something, respectively. The first one will print True, as the string starts with "Hello". The second one will print False, as the string certainly does not end with "asdfasdfasdf"."""

tstring = "Hello world!"
fewwords = tstring.split("Hello world!")
print(fewwords)

string = "welcome to the jungle"

x = string.split()

print(x)

"""**Exercise**
Try to fix the code to print out the correct information by changing the string.
"""

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

"""**Conditions**

Python uses *boolean logic* to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. For example:
"""

x = 2
print(x == 2)
print(x == 3)
print(x < 398)

"""the variable assignment is done using a single equals operator "=",
whereas comparison between two variables is done using the double equals operator "==".
The "not equals" operator is marked as "!=".

***Boolean operators***

The "and" and "or" boolean operators allow building complex boolean expressions, for example:
"""

name = "John"
age = 23
if name == "John" and age == 23:
  print(" Your name is John, and you are also 23 years old ")
  if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

"""**The "in" operator**


The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
"""

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

"""Python uses **indentation **to define code blocks, instead of brackets. **The standard Python indentation is 4 spaces**, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination."""

statement = False
another_statement = True
if statement is True:
    # do something
    print("statement = true")
    pass
elif another_statement is True: # else if
    # do something else
    print (" Statement is " ,statement )
    print ("another_statement = True")
    pass
else:
    # do another thing

    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

"""A statement is evaulated as true if one of the following is correct: 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 2. An object which is not considered "empty" is passed.

Here are some examples for objects which are considered as empty: 1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False

**The 'is' operator**

Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
"""

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

"""The "not" operator


Using "not" before a boolean expression inverts it:

**Exercise**


Change the variables in the first section, so that each if statement resolves as True.
"""

# change this code
number = 16
second_number = 10
first_array = [1,0]
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number == 4:
    print("6")
