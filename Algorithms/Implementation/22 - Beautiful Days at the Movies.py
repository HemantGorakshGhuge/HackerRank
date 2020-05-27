#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(num):
    rev = 0
    while(num > 0): 
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    return rev

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    num = i
    count = 0
    while(num <= j):
        if (abs(num-reverse(num)))%k == 0:
            count+=1
        print(count)
        num+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
