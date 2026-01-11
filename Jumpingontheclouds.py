#!/usr/bin/env python
# coding: utf-8

# #### Jumping on the Clouds: Revisited
# 
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=false

# In[ ]:


def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    pos = 0
    while True:
        pos = (pos + k) % n
        if c[pos] == 0:
            energy -= 1 
        else:
            energy -= 3
        if pos == 0:
            break

    return energy

