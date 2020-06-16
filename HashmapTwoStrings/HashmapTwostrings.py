#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    sauce = dict()
    for i in range(len(s1)):
        sauce[s1[i]] = 1

    for j in range(len(s2)):
        if s2[j] in sauce.keys():
            return "YES"

    return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
