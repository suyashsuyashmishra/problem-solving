#!/usr/bin/env python
# coding: utf-8

# #### question on 
# 
# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false

# In[8]:


def timeConversion(s):
    time_split=s.strip()
    time_part = time_split[:-2]
    meridian = time_split[-2:].upper()
    
    hours,minutes,seconds = map(int,time_part.split(":"))
    if meridian == "AM":
        if hours == 12:
            hours=0
    elif meridian == "PM":
        if hours != 12:
            hours+=12
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# In[ ]:





# In[ ]:




