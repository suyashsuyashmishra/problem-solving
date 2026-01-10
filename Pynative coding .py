#!/usr/bin/env python
# coding: utf-8

# #### Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

# In[23]:


prev_num= 0
print("Printing current and previous number sum in a range(10)")
for i in range(0,10):
    sum = prev_num + i
    print("Current Number",i,"Previous Number",prev_num,"sum:",sum) 
    prev_num = i


# #### Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
# 
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# In[26]:


n = input()
for i in n[::2]:
    print(i)


# #### Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

# In[1]:


original_string = input("Enter a string: ")
remove_chr = int(input("Enter number of characters to remove: "))


if 0 <= remove_chr <= len(original_string):
    new_string = original_string[remove_chr:]
    print("New string:", new_string)
else:
    print("Invalid number of characters to remove")

    



# #### Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# In[19]:


first_list = list(map(int, input("Enter the values in the first list: ").split()))
second_list = list(map(int,input("Enter the values in the second list: ").split()))

print ("The value in the first list is:", first_list)
print ("The value in the second list is:", second_list)

if first_list[0]==second_list[len(second_list)-1]:
    print(True)
else:
    print(False)


# #### Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

# In[1]:


list_div = list(map(int, input("Enter the values in the list: ").split()))
print ("The value in the list is:", list_div)

def five_multiple(lst):
    final_list = []
    for i in lst:
        if i%5==0:
            final_list.append(i)
            
    return final_list
print(five_multiple(list_div))


# #### Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.

# In[1]:


str_x = input("Enter the string: ")
word_input = input("Enter the word to check weather the word is repeated: ")
count = str_x.count(word_input)
print("Word", word_input, "appears", count, "times in string")




# #### Exercise 8: Print the following pattern
# 1 
# 
# 2 2
# 
# 3 3 3
# 
# 4 4 4 4 
# 
# 5 5 5 5 5

# In[13]:


for i in range(1,6):
    for j in range(i):
        print(i,end = " ")
    print()
  


# #### Exercise 9: Check Palindrome Number
# 
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# In[8]:


input_number = int(input("Enter the number: "))
original_number = input_number
check_palindrome = 0
while(input_number != 0):
    remainder_number = input_number%10
    check_palindrome = check_palindrome * 10 + remainder_number
    input_number = input_number//10
if(check_palindrome==original_number):
    print(original_number,"is a palindrome.")
else:
    print("Not a palindrome!!")
    
    

    


# #### Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
# 
# Given:
# 
# list1 = [10, 20, 25, 30, 35]
# 
# list2 = [40, 45, 60, 75, 90]
# 
# Expected Output:
# 
# result list: [25, 35, 40, 60, 90]

# In[9]:


list1 = list(map(int, input("Enter the values in the first list: ").split()))
list2 = list(map(int,input("Enter the values in the second list: ").split()))

odd_list = []
even_list = []
result_list = []

for i in list1:
    if (i%2 != 0):
        odd_list.append(i)
for j in list2:
    if(j%2==0):
        even_list.append(j)
        
result_list = odd_list + even_list
print(result_list)
    


# #### Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
# 
# Given:
# 
# number = 7536
# # Output 6 3 5 7

# In[12]:


original_number = int(input("Enter the number: "))
while(original_number>0):
    remainder_number = original_number%10
    original_number = original_number//10
    print(remainder_number, end = " ")


# #### Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
# 
# Taxable Income	Rate (in %)
# 
# First $10,000	0
# 
# Next $10,000	10
# 
# The remaining	20
# 
# Expected Output:
# 
# For example, suppose the income is 45000, and the income tax payable is:
# 
# 10000*0% + 10000*10%  + 25000*20% = $6000

# In[5]:


amount_provided = int(input("Provide the amount: "))
tax = 0
if amount_provided<=10000:
    tax = 0
if (10000<amount_provided<=20000):
    tax = tax+ 10000*0 +(amount_provided-10000)*0.1
if (amount_provided>20000):
    tax =  tax+ 10000*0 + (10000*0.1) + (amount_provided-20000)*0.2
print("The income tax payable is $",tax)



# #### Exercise 13: Print multiplication table from 1 to 10
# 
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
# 
# Write a code to generates a complete multiplication table for numbers 1 through 10.
# 
# Expected Output:
# 
# 1  2 3 4 5 6 7 8 9 10 	
# 
# 2  4 6 8 10 12 14 16 18 20 	
# 
# 3  6 9 12 15 18 21 24 27 30 
# 
# 4  8 12 16 20 24 28 32 36 40 	
# 
# 5  10 15 20 25 30 35 40 45 50 
# 
# 6  12 18 24 30 36 42 48 54 60 
# 
# 7  14 21 28 35 42 49 56 63 70 
# 
# 8  16 24 32 40 48 56 64 72 80 
# 
# 9  18 27 36 45 54 63 72 81 90 
# 
# 10 20 30 40 50 60 70 80 90 100

# In[25]:


for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = " ")
    print()


# #### Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# In[72]:


str = "*"
for i in range(5,0,-1):
    for j in range(i):
        print(str, end = " ")
    print()
    
    


# #### Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# 
# Note here exp is a non-negative integer, and the base is an integer.
# 
# Expected output
# 
# Case 1:
# 
# base = 2
# exponent = 5
# 
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
# Case 2:
# 
# base = 5
# exponent = 4
# 
# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

# In[3]:


a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))
def exponent(base, exp):
    result = 1
    for i in range(exp):
        result*= base
    return result

print(a,"raises to the power of",b,"is:",exponent(a,b))    


# #### Exercise 16: Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
# 
# Write a code to check if given number is palindrome.

# In[6]:


input_number = int(input("Enter the number: "))
original_number = input_number
check_palindrome = 0
while(input_number != 0):
    remainder_number = input_number%10
    check_palindrome = check_palindrome * 10 + remainder_number
    input_number = input_number//10
if(check_palindrome==original_number):
    print(original_number,"is a palindrome.")
else:
    print("Not a palindrome!!")
    


# #### Exercise 17: Generate Fibonacci series up to 15 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# 
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

# In[19]:


first_number = 0
second_number = 1

for i in range(1,16):
    print(first_number, end = " ")
    result = first_number+second_number
    first_number = second_number
    second_number = result
    
   
        
    


# #### Exercise 18: Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
# 
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
# 
# Write a code find if a given year is a leap year.

# In[14]:


enter_year = int(input("Enter the year: "))

if enter_year <= 0:
    print("Year must be positive")
elif (enter_year % 400 == 0) or (enter_year % 4 == 0 and enter_year % 100 != 0):
    print("Leap Year")
else:
    print("Not a leap year")


        


# #### Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
# 
# For example:
# 
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
# 
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

# In[62]:


def prime_number(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

primes = [n for n in range(1,21) if prime_number(n)]

alternatives_primes = primes[::2]


print("All primes till 20:", primes)
print("Alternate primes till 20:", alternatives_primes)   


# #### Exercise 20: Print Reverse Number Pattern
# Expected Output:
# 
# 1 1 1 1 1 
# 
# 2 2 2 2 
# 
# 3 3 3 
# 
# 4 4 
# 
# 5 

# In[70]:


for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i, end = " ")
    print()


# #### Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:
# 
# Enter a string: Pynative123Python
# 
# The string contains at least one digit.
# 
# Enter a string: PYnative
# 
# The string does not contain any digits.

# In[ ]:


def contain_digit(text):
    for char in text:
        if ("0"<= char<= "9"):
            return True
    return False
    
my_string = input("Enter a string: ")

if contain_digit(my_string):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")
            
    


# #### Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:
# 
# str1 = "pynative.com is for python lovers"
# 
# ### Output Pynative.com Is For Python Lovers
#             

# In[41]:


str_1 = input()
str_2 = str_1.capitalize()
print(str_2)


# #### Exercise 23: Create a simple countdown timer using a while loop.
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
# 
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
# 
# Expected Output:
# 
# Time remaining: 5 seconds
# 
# Time remaining: 4 seconds
# 
# Time remaining: 3 seconds
# 
# Time remaining: 2 seconds
# 
# Time remaining: 1 seconds
# 
# Time's up!

# In[52]:


def countdown_timer(t):
    
    while (t>0):
        print("Time remaining:",t,"seconds")
        t = t-1
    print("Time's up!")
countdown_timer(5)
    


# # INPUT AND OUTPUT PYTHON EXCERSIZE

# #### Exercise 1: Accept Numbers From User
# Write a program to accept two integer numbers from the user and calculate their product.

# In[54]:


def product_calculator(a,b):
    c = a*b
    return c


integer_1 = int(input())
integer_2 = int(input())

product_calculator(integer_1,integer_2)


# #### Exercise 2: Format Output String
# Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
# 
# Use the print() function to format the given words in the specified format. Display the ** separator between each string.
# 
# Given:
# 
# str1 = 'My'
# 
# str2 = 'Name'
# 
# str3 = 'Is'
# 
# str4 = 'James'
# 

# In[55]:


str1 = 'My'

str2 = 'Name'

str3 = 'Is'

str4 = 'James'

print(str1,"**",str2,"**",str3,"**",str4)


# #### Exercise 3: Display Decimal Number to Octal using print() function
# Given:
# 
# num = 8

# In[60]:


num = 8

print('%o'%num)


# #### Exercise 4: Display Float Number with 2 Decimal Places
# Given:
# 
# num = 458.541315
# 
# Expected Output:
# 
# 458.54

# In[ ]:


n,m = map(int, input().split())
print(n,m)




# In[ ]:




