#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    offset = 1
    result = 0
    memo = {}

    while offset <= len(s):
        L = 0
        R = L + offset

        while R <= len(s):
            anagram = ''.join(sorted(s[L:R]))
            if anagram in memo:
                memo[anagram] += 1
            else:
                memo[anagram] = 1
            R += 1
            L += 1

        offset += 1

    for i in memo:
        if memo[i] > 1:
            result += (memo[i])*(memo[i]-1)/2
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
