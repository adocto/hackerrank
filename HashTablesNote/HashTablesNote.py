#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    messageWords = dict()
    possible = True

    for word in magazine:
        if word in messageWords:
            messageWords[word] += 1
        else:
            messageWords[word] = 1

    for word in note:
        if word in messageWords:
            if messageWords[word] > 0:
                messageWords[word] -= 1
            else:
                possible = False
        else:
            possible = False

    if possible is True:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
