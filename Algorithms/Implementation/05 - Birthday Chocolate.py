#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
#m -> length
#d -> sum
def birthday(s, d, m):
    end = True
    Ron_bar = 0
    i = 0
    while (end == True):
        segments = s[i:m+i]
        print(segments)
        if sum(segments) == d:
            Ron_bar += 1
        if i == len(s)-m:
            end = False
        i+=1
    return Ron_bar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
