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
