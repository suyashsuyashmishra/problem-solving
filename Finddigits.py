#!/usr/bin/env python
# coding: utf-8

# #### Find Digits
# 
# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=false

# In[1]:


def findDigits(n):
    count = 0
    for i in str(n):
        digit = int(i)
        if(digit!=0 and n%digit==0):
            count+=1
    return count


# In[ ]:




