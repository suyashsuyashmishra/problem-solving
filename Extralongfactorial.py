#!/usr/bin/env python
# coding: utf-8

# #### Extralongfactorial
# 
# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=false

# In[1]:


def extraLongFactorials(n):
    # Write your code here
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    print(factorial)


# In[ ]:




