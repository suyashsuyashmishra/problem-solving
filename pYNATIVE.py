#!/usr/bin/env python
# coding: utf-8

# Exercise 1: List Comprehension Mastery
# 
# Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
# 
# Exercise Purpose: List comprehensions are a hallmark of Pythonic code. They allow you to replace verbose for loops and .append() calls with a readable, optimized single line. This exercise teaches you how to combine transformation (uppercase) and filtering (length check) in one expression.
# 
# Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]
# 
# Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']

# In[7]:


def longstring(arr):
    newstring = []
    for i in range(len(arr)): 
        if(len(arr[i])>4):
            newstring.append(arr[i].upper())
    return newstring

arr = input("Enter words: ").split()

print(longstring(arr))





        


# Exercise 2: Dictionary Merging with Logic
# 
# Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
# 
# Exercise Purpose: Real-world data often comes from multiple sources. Simply using dict.update() would overwrite duplicate keys. This exercise introduces you to efficient dictionary iteration and the dict.get(key, default) method, which is essential for avoiding KeyError.
# 
# Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}
# 
# Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

# In[16]:


def mergeddict(a, b):
    a_values = a.values()
    b_values = b.values()
    new_values = [a[k] + b[k] for k in a.keys() & b.keys()]
    all_keys = a.keys() | b.keys()
    finaldict = {k: a.get(k, 0) + b.get(k, 0) for k in all_keys}
    
    return finaldict

import json

dict_a = json.loads(input("Enter first dict (JSON): "))
dict_b = json.loads(input("Enter second dict (JSON): "))

print(mergeddict(dict_a, dict_b))


# Exercise 3: Frequency Map with Counter
# 
# Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.
# 
# Exercise Purpose: While you could build a frequency map with a standard loop, Python’s collections module offers a specialized tool called Counter. This exercise teaches you to leverage the Standard Library to write less code while increasing performance.
# 
# Given Input: text = "Python Programming"

# In[40]:


def frequencymap(m):
    unique_values = new_m - " "
    unique_list = [unique_values]
    for i in m:
        print({unique_values:m.count(i)})
     
    
m = input()
frequencymap(m)
frequencymap(m)
frequencymap (m)
frequencymap(m)


# In[ ]:





# In[ ]:





# In[ ]:




