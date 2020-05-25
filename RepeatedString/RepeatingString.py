#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #While i <=n
    i = 0
    j = 0
    result = 0
    if 'a' in s:
        if len(s) == 1:
            result = n
        else:
            j = 0
            while i < n:
                # if s[j] == a, result ++
                if s[j] == 'a':
                    result += 1
                #i++,
                i += 1
                #   if j < lens -1 j++
                if j < len(s)-1:
                    j+=1
                #   else j = 0
                else:
                    j = 0
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
