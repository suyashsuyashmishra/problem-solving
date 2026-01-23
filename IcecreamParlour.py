#!/usr/bin/env python
# coding: utf-8

# https://www.hackerrank.com/challenges/icecream-parlor/proble

# In[44]:


def icecreamParlor(m, arr):
    
    seen = {}  # hashmap: value -> index
    
    for i, num in enumerate(arr):
        complement = m - num
        if complement in seen:
            # return 1-based indices
            return seen[complement] + 1, i + 1
        seen[num] = i

