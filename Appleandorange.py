#!/usr/bin/env python
# coding: utf-8

# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

# In[44]:


def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesdistance = [i+a for i in apples]
    orangesdistance = [j+b for j in oranges]
    applecount = 0
    orangecount = 0
    for k in applesdistance:
        if(s<=k<=t):
            applecount += 1
    for l in orangesdistance:
        if(s<=l<=t):
            orangecount += 1
    print(applecount)
    print(orangecount)

