#!/usr/bin/env python
# coding: utf-8

# ### Capitalise
# 
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# In[14]:


def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

