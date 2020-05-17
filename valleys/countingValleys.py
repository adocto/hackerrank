#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    result = 0
    for i in range(n):
        if height == 0:
            val_flag = True
        else:
            val_flag = False
        if s[i] == 'U':
            height += 1
        elif (s[i] == 'D') and (val_flag == True):
            height -= 1
            result += 1
        else:
            height -= 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
