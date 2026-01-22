#!/usr/bin/env python
# coding: utf-8

# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

# In[ ]:


def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    return result

