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

    def checkMatch(sub,sub2):
        SubString1 = ''.join(sorted(sub))
        SubString2 = ''.join(sorted(sub2))
        if SubString1 == SubString2:
            return 1
        else:
            return 0

    while offset <= len(s):
        L = 0
        R = L + offset

        while R <= len(s):
            L2 = L + 1
            R2 = L2 + offset
            # anagram = ''.join(sorted(s[L:R]))
            # if anagram in memo:
            #     result += 1
            # else:
            #     memo[anagram] = 1
            while R2 <= len(s):
                anagram = checkMatch(s[L:R],s[L2:R2])
                result += anagram
                R2 +=1
                L2 +=1
            R += 1
            L += 1
        offset += 1
    return result





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
