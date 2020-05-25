#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #drawer Arr 100
    drawer = {}
    i = 0
    result = 0
    #While i < N
    while i < n:
    #if not in drawer
        if ar[i] not in drawer:
            drawer[ar[i]] = 1
    #else drawer [ar[i]] =1
        elif drawer[ar[i]] == 0:
            drawer[ar[i]] = 1
        else:
            drawer[ar[i]] = 0
            result += 1
        i+=1
    #return pairs
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
