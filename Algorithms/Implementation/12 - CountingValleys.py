#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    list_s = list(s)
    count = 0
    count_prev = 0
    valley = 0
    for l in list_s:
        if l == 'D':
            count -=1
        elif l == 'U':
            count +=1
        if count_prev < 0 and count == 0:
            valley +=1
        count_prev = count
        
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
