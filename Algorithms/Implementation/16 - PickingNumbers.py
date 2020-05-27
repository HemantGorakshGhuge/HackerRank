#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count=0
    length = []
    a = sorted(a)
    print(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if j>i:
                if abs(a[i]-a[j])<=1:
                    count+=1
                elif count!=0:
                    length.append(count)
                    count=0
                    break
                else:
                    break
    if not length:
        length.append(len(a)-1)
    print(length)
    return(max(length)+1)

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
