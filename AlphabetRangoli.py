#!/usr/bin/env python
# coding: utf-8

# ### Alphabet Rangoli
# 
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

# In[14]:


import string

def print_rangoli(size: int) -> None:
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        s = alpha[size-1:size-1-i:-1] + alpha[size-1-i:size]
        row = "-".join(s)
        lines.append(row.center(width, "-"))

    rangoli = lines + lines[-2::-1]
    print("\n".join(rangoli))

