#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 1
    if n > 2:
        if c[2] == 0:
            i = 2
        else:
            i = 1
        while i < n-2:
            if c[i+2] == 0:
                jump = 2
            else:
                jump = 1
            i += jump
            result += 1
        if i == n-2:
            result +=1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
