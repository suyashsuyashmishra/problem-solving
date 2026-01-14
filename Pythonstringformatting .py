#!/usr/bin/env python
# coding: utf-8

# ### Python String Formatting
# 
# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

# In[14]:


def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

