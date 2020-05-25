#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    i = 0
    j = 0
    result = 0
    if 'a' in s:
        if len(s) == 1:
            result = n
        elif len(s) < n:
            multiplier = n // len(s)
            runoff = n % len(s)
            j = 0
            while i < len(s):
                if s[i] == 'a':
                    result += 1
                i+=1
            result = result * multiplier
            while j < runoff:
                if s[j] == 'a':
                    result +=1
                j+=1
        else:
            while i < n:
                if s[i] == 'a':
                    result +=1
                i+=1
    return result

# def checkOnlyA(s):
#     j = 0
#     onlyA = True
#     while j < len(s) - 1 and onlyA == True:
#         if s[j] != 'a':
#             onlyA = False
#     return onlyA

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
