#!/usr/bin/env python
# coding: utf-8

# #### Birthday candle cake question:
# 
# URL:https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=false

# In[ ]:


def birthdayCakeCandles(candles):
    tall = max(candles)
    return candles.count(tall)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

