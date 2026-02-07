"""#using break in while loop
number=[25,30,20,40,15,25]
total=0
i=0
while i<len(number):
    total+=number[i]
    if total>100:
        print("sum exceeded 100")
        break
    i+=1
else:
    print(total) 
#using continue in for loop
for i in range(1,600):
    if i%2!=1:
        continue
    print("odd numbers",i)
#using pass in conditional statement
for i in range(1,100):
    if i%2==0:
        print("even number:",i)
    else:
        pass  """
#combine the transfer statements

"""words=["hi","hello","break","byee","skip","continue"]
for word in words:
    if word=="break":
        break
    elif word=="skip":
        continue
    else:
        print(word)"""
#reverse a list
"""my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)
#common elements
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_eliments=[x for x in list1 if x in list2]
print(common_eliments)
#unique elements
original_list=[1,2,2,3,4,4,5]
unique_elements=[]
for i in original_list:
    if i not in unique_elements:
        unique_elements.append(i)
print(unique_elements)
# list concantination
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
print(f"{list1 +list2}") 
#list repitation
list1=[1,2,3,4,5]
list_repetition=list1*3
print(list_repetition)

#list removal
numbers=[10,20,30,40,50]
result=[]
for i in range (len(numbers)):
    if i%2!=0:
        result.append(numbers[i])
print(result)
"""
"""Expected output:

1
2
3
4
5
6
7
8
9
10

i=1
while i <=10:
    print(i)
    i+=1"""
"""Write a Python code to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5"""
"""row=10
b=0
for i in range(row,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end='')
    print("")   """ 
"""a,b,*c,d=[1,2,3,4,5,6,7]
print(c)"""
"""
 Learn Python
Python Tutorials
 
Python Basics
 
Python Interview Q&As
 
 Exercises
Python Exercises
 
C Programming Exercises
 
C++ Exercises
 
 Quizzes
 
 Code Editor
Online Python Code Editor
 
Online C Compiler
 
Online C++ Compiler
Search this website
Home » Python » Python Programs to Print Patterns – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Python Programs to Print Patterns – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Updated on: September 3, 2024 | 457 Comments

This Python lesson includes over 35+ coding programs for printing Numbers, Pyramids, Stars, triangles, Diamonds, and alphabet patterns, ensuring you gain hands-on experience and confidence in your Python skills.

Printing numbers, stars (asterisk), or other characters in different shapes (patterns) is a frequently asked interview question for freshers. Creating these number and pyramid patterns allows you to test your logical ability and coding skills.

In this lesson, you’ll learn how to print patterns using the for loop, while loop, and the range() function.

This article teaches you how to print the following patterns in Python.

Number pattern
Pyramid pattern
Inverted pyramid pattern
Half pyramid pattern
Triangle pattern
Star (*) or asterisk pattern
Diamond Shaped pattern
Characters or alphabet pattern
Square pattern
Print Pattern in Python
Print Pattern in Python
Table of contents
Steps to Print Pattern in Python
Number Patterns Programs In Python
Pyramid pattern of numbers
Inverted pyramid pattern of numbers
Inverted Pyramid pattern with the same digit
Another inverted half-pyramid pattern with a number
Alternate numbers pattern using a while loop
Reverse number pattern
Reverse Pyramid of Numbers
Another reverse number pattern
Print reverse number from 10 to 1
Number triangle pattern
Pascal’s triangle pattern using numbers
Square pattern with numbers
Multiplication table pattern
Pyramid pattern of stars in python
Right triangle pyramid of Stars
Downward half-Pyramid Pattern of Star
Downward full Pyramid Pattern of star
Right down mirror star Pattern
Equilateral triangle pattern of star
Print two pyramids of stars
Right start pattern of star
Left triangle pascal’s pattern
Sandglass pattern of star
Pant style pattern of stars
Diamond-shaped pattern of stars
Another diamond pattern of star
Alphabets and letters pattern
Pattern to display letter of the word
Equilateral triangle pattern of characters/alphabets
Pattern of same character
More miscellaneous Patterns
Pyramid of horizontal number tables
Double the number pattern
Random number pattern
Pyramid of numbers less than 10
Pyramid of numbers up to 10
Even number pattern
Unique pyramid pattern of digits
Pattern double number on each column
Number reduction pattern
Pant style pattern of numbers
Pattern with a combination of numbers and stars
Practice Problem
Next Steps
Steps to Print Pattern in Python
To print any pattern, you must first understand its logic and technique. Use the below steps to print any pattern in Python.

Decide the number of rows and columns
The number of rows and columns is crucial when printing a pattern. To achieve this, we utilize two loops: outer loops and nested loops. The outer loop is the number of rows, while the inner loop tells us the column needed to print the pattern.

The input () function accepts the number of rows from a user to decide the size of a pattern.

Iterate rows
Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

Iterate columns
Next, write the inner or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

Print star or number
Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

Add a new line after each iteration of the outer loop
Add a new line using the print() function after each iteration of the outer loop so that the pattern displays appropriately

Algorithm for printing patterns in Python
Algorithm for printing patterns in Python
Also, Solve:

Python loop exercise
Python Basic Exercise for Beginners
Number Patterns Programs In Python
I have created various programs that print different styles of number patterns. Let’s see them one by one. Let’s print the following number pattern using a for loop.

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
 Run
In this number pattern, we display a single digit on the first row, two digits on the second row, and three digits on the third row. This process will repeat until the number of rows is reached.

Note:

The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.

Program:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
 Run
Inverted pyramid pattern of numbers
An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
 Run
Inverted Pyramid pattern with the same digit
Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
 Run
Alternate numbers pattern using a while loop
Let’s see how to use the while loop to print the number pattern.

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
 Run
Reverse number pattern
Let’s see how to display the pattern of descending order of numbers

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
This pattern is also called as a inverted pyramid of descending numbers.

Program: 

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Reverse Pyramid of Numbers
Pattern 2: –

""""""Pattern: –

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1"""
"""n=5
for  i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()    
"""
"""n=5
for i in range(1,n+1):
    for j in range(i-1):
        print("_",end=" ")
    for k in range(1,n-i+2):
        print(k,end=" ")  
    print()      
"""
# Account details
owner = "bharath"
balance = 0

def show_menu():
    print("\n==============================")
    print("Welcome to ATM")
    print("Account Holder:", owner)
    print("==============================")
    print("1. Credit (Deposit)")
    print("2. Debit (Withdraw)")
    print("3. Check Balance")
    print("4. Exit")


def credit():
    global balance
    amount = float(input("Enter amount to credit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    else:
        balance += amount
        print("Amount credited successfully.")
        print("Updated Balance: ", balance)


def debit():
    global balance
    amount = float(input("Enter amount to debit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Amount debited successfully.")
        print("Updated Balance: ", balance)


def check_balance():
    print("Account Holder:", owner)
    print("Current Balance: ", balance)


def atm():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Thank you,", owner)
            print("Please visit again.")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")


atm()















        

    
           
