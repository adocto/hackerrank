#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    print(toss[0])
    max_heads = 0
    max_tails = 0
    tails = 0
    heads = 0
    n = 0
    for n in range(len(toss)):
        print(heads)
        print(tails)
        if n == 0:
            if toss[n] == 'Heads':
                heads +=1
            else:
                tails +=1
        else:
            if (toss[n-1] == 'Heads' and toss[n] == 'Heads'):
                heads +=1
                if heads > max_heads:
                    max_heads = heads
            elif (toss[n-1] == 'Tails' and toss[n] == 'Tails'):
                tails +=1
                if tails > max_tails:
                    max_tails = tails
            elif (toss[n-1] == 'Heads' and toss[n] == 'Tails'):
                tails = 1
                heads = 0
            else:
                tails = 0
                heads = 1
    ans = max_heads, max_tails
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
