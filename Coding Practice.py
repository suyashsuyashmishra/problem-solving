#!/usr/bin/env python
# coding: utf-8

# #### Problem Statement: Plus Minus
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
# 
# Function Description
# Complete the function plusMinus in the editor below.
# plusMinus has the following parameter(s):
# - int arr[n]: an array of integers
# 
# Print
# Print the following 3 lines, each to 6 decimal places:
# - The fraction of positive numbers in the array
# - The fraction of negative numbers in the array
# - The fraction of zeros in the array
# 
# Input Format
# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].
# 
# Constraints
# - 0<n\leq 100
# - -100\leq arr[i]\leq 100
# 
# Output Format
# Print the following 3 lines, each to 6 decimal places:
# - proportion of positive values
# - proportion of negative values
# - proportion of zeros
# 
# Sample Input
# 6
# -4 3 -9 0 4 1
# 
# 
# Sample Output
# 0.500000
# 0.333333
# 0.166667
# 
# 
# 
# Explanation
# There are 6 elements in the array:
# - 3 positive numbers → fraction = 3/6=0.500000
# - 2 negative numbers → fraction = 2/6=0.333333
# - 1 zero → fraction = 1/6=0.166667
# 
# 
# 

# In[ ]:


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if(i>0):
            positive += 1
        elif(i<0):
            negative+= 1
        else:
            zero+= 1
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")


# ### Staircase
# This is a staircase of size n:
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# 
# 
# Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.
# 
# Function Description
# Complete the function staircase with the following parameter(s):
# - int n: an integer
# Print
# Print a staircase as described above. No value should be returned.
# Note:
# - The last line is not preceded by spaces.
# - All lines are right-aligned.
# 
# Input Format
# A single integer, n, denoting the size of the staircase.
# 
# Constraints
# - 0<n\leq 100
# 
# Output Format
# Print the staircase of size n using # symbols and spaces.
# 

# In[1]:


def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)

    


# In[3]:


staircase(9)


# ### Mini-Max Sum
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# 
# Example
# arr = [1, 3, 5, 7, 9]
# 
# 
# - The minimum sum is 1 + 3 + 5 + 7 = 16.
# 
# - The maximum sum is 3 + 5 + 7 + 9 = 24.
# 
# The function prints:
# 16 24
# 
# 
# 
# Function Description
# Complete the function miniMaxSum in the editor below.
# miniMaxSum has the following parameter(s):
# 
# - arr: an array of 5 integers
# 
# Print
# Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of the 5 elements.
# 
# Input Format
# A single line of five space-separated integers.
# 
# Constraints
# 
# - 1\leq arr[i]\leq 10^9
# 
# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values.
# 

# In[ ]:


def MiniMaxSum(arr):
    n = len(arr)
    for i in 
    

