# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:49:14 2021

@author: Gowtham S
"""

# Comments
x = 10 # X has the value of 10

# Gowtham - This is a comment
'''
This is multiple
line comment
'''


# Variables
# A-Z, a-z, 0-9, _

x = 10
y = 28

myVar = 100

my_name = "gowtham"

# Intialisation / declaration
#2myvar = 10
#my-var = 10
#my var = 100

# Programming Etiquettes

my_var = 10 # Snake Case

myVar = 10 # Camel Case

MyVar = 10 # Pascal Case

my_name = "gowtham" # Meaninful names


# Case Sensitive

my = 10

My = 20
# Data Types
# int, str, float

x = 10

y = 12.9

name = "gowtham"
cha = "g"

x_str = "10"

# Type Casting

y_int = int(y)

name_int = int(name)

x_num = int(x_str)

# Print and Input

x = 10
print("Value of x: ",x)

x = int(input("Enter the value: "))


# Arithmetic Operators
# +, *, -, /, %, //, **

c = 1 + 5

c = 12 * 4

4 / 2

5 // 2 # Floor division

4 % 2 # Modulus


Assignment-0
1. Write Algorithm for finding x and y from the below sequence:
	10, 1, 8, 3, 6, 5, 4, 7, x, y

2. "end" in print function of python - google

3. Revision of what so far is done

Submitting Procedure:
1. Create a new repository - without MyCaptain name.

2. Upload ur code in that repo.

3. Submit link will be given next week.



# Assignment Operator

# =

x = 5

y = x


y += 2
y = y + 2

y *= 3
y = y * 3







# Comparison Operators

>, <, ==, !=, <=, >=

==

!=

x = 6
y = 6

y > x

x != y

True and False = Boolean Data Types



# Logical Operator

and, or, not

x = 5
y = 6

y > x and y != x

# Not code
y > x = True
y != x = True
True and True = True (Truth Tables)
True and False



# If statement

Turing Complete Program - logical programs
Logical or not - if, else and Loops

Turing - Alan Turing - winner of ww2
Turing Test - Participated - Captcha
Immitation Games - movie

x = 5
y = 5

if x==y:
    print("Equal")
elif y>x:
    print("Greater")


Assignment 1.1:

1. Use opertaors - <, <=, >, >=, or, not
2. Create a simple calculator.
    
sample:
1. It should ask for two inputs,
    a. choice,
        1. Add
        2. Subtract
        enter choice: 1
    b. The values,
        enter a: 1
        enter b: 3
Sum: 4
- Complete Creative freedom







# Functions

def add(a, b):
    print(a+b)

def add(a, b):
    return a+b

add(1, 2) # calling
add(2, 3)

c = add(10, 50)
print(c)



# List
# Ordered and Changeable

l1 = [1, 2, 3, 4.5, 20, 30, "gowtham"]


l1[4]

# add
l1.append(33)

# Remove
l1.pop()


# Strings
l1 = ["g", "o"]

s1 = "go"

l1[0]

s1[0]

s1[0:2]


Assignment 1.2:

1. Implement Lists and String methods (w3schools)

2. Create a calculator using functions

Submission Procedure:

1. Google forms link on Sunday
2. Paste the github link to a new repo of the projects
3. Deadline is 12:30 AM (Morning) - Monday (18th October)


# Some questions

l1 = [1, 2, 3, "gowtham"]

1. Add an integer to  the end of the list - append

2. Delete an integer to  the end of the list - pop

3. Change the value 3 to 4 - replace

l1[2] = 4

x = 3
x = 4


# Tuples
# Immutable - Cannot be changed or manipulated
   # cannot add or remove or anything
# Ordered or Unordered ?? - Ordered - Indexed

l1 = [1, 2, 3, "gowtham"]

t1 = (1, 2, 3, "gowtham")

t1[0]

# Use ??
# Saving lot of data and accessing them faster - 10000 entries


# Dictionary
# Store values as a pair - Key and Value Pair

A - Words that starts with A

Key - A
Values - Words that begin with A

d1 = {"name":"gowtham", "age":23, "dep":"CS", "marks":[1, 2, 3]}

d1["name"]

# Changed value
CS to CSE

d1["dep"] = "CSE"

# You cannot change the value of a key
# Key has to be unique
# Question of the day:
Google:
1. How will you change values in a Tuple ? clue: Typecasting
2. How will you change the value of a key ?


# Loops - For and While
# Turing Complete Program - do you remember it ?

l1 = [1, 2, 3, "gowtham"]

l1[1:3]

for i in range(1, 6):
    print(i)

length of l1 = ??

len(l1)

for i in range(0, len(l1)):
    print(l1[i])



for element in l1:
    print(element)


Assignment 2.1:

1. Methods of Dictionary (w3schools) - TBI
2. Study on Sets (w3schools)
3. For loops - Step Function - TBI
4. For loop - triangle pattern - TBI
    *
   * *
  * * *
 * * * *

Google:
1. How will you change values in a Tuple ? clue: Typecasting
2. How will you change the value of a key ?

Use internet but do not copy and paste code, TYPE IT

TBI - To Be Implemented 



# While

for i in range(0, 11):
    print(i)

explicit - in detail, given by the creator
implicit - it is by default


i = 0
while i<11:
    i = i+1
    print(i)

l1 = [11, 23, 45, 67]

for element in l1:
    print(element)


Is it right? If not then what is the problem?

i = 0
while i<len(l1):
    print(l1[i])
    i = i+1


length = ?? (4)
What is the index value of last number ? (3)

l1[4]

Solution? - only cut paste a line no changes


# Recursion

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

fact(4)





One difference between Packages and API ??
1. P: Free, A: Not Free
2. P: Local, A: Depends on External(company) Server




import functions.arithmetic as alias

alias.addition(2, 3)



l1 = [0, 1, 2]

2+ 3

l1[3] # Index Error

1 + 2


Python - Uses Interpreter 

5
Error
3

Or

5
Error - Stops


import requests
from bs4 import BeautifulSoup

urls = ["https://www.amazon.in/United-Colors-Benetton-Sneakers-11-19P8SNEA3113I_902_40/dp/B07L58JVGV/ref=pd_d0_recs_v4_ac_w2_22/258-3905153-5220442?pd_rd_w=1uyYc&pf_rd_p=d07e23a0-088f-4edf-84b9-2836fb74cf31&pf_rd_r=4TKKTDR8TCG1WV73P70B&pd_rd_r=e725627d-a833-48c0-8d14-1869b648be09&pd_rd_wg=thhbR&pd_rd_i=B07LGJZ3YP&th=1&psc=1"]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

page = requests.get(urls[0], headers=headers)

#page.content

soup = BeautifulSoup(page.content, parser='html.parser')

title = soup.find(id="productTitle").get_text()

price = soup.find(id="priceblock_ourprice").get_text()

-- Send me a message saying the price has reduced



# Class
class Car:
    def __init__(self, wheels, doors):
        self.wheels = wheels
        self.doors = doors
    
    def disp(self):
        print("The car has ", self.wheels, " wheels")


lambo = Car(4, 2)
lambo.disp()

bean_rival = Car(3, 4)
bean_rival.disp()

How does python knows the value of 4 belongs to lambo
and value of 3 belongs to bean_rival ?? - Self


l1 = [1, 2, 3, 4]
l2 = [10, 12, 56]

l1.append(5)
l2.append(555)


















