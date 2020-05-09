#!/bin/python3

import math
import os
import random
import re
import sys

def distance(a, b):
    if (a <= 0) and (b <= 0) or (a >= 0) and (b >= 0):
        return abs( abs(a) - abs(b) )
    elif (a <= 0) and (b >= 0) or (a >= 0) and (b <= 0):
        return abs( abs(a) + abs(b) )

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    dist1 = x1
    dist2 = x2
    
    if x1>x2:
        print('x1>x2')
        init_gap = distance(dist1, dist2)
    elif x2>x1:
        init_gap = distance(dist2, dist1)
    else:
        return 'YES' 

    print('init_gap = {}'.format(init_gap))

    while(True):
        dist1 = dist1 + v1
        dist2 = dist2 + v2

        if dist1 == dist2: #both came at same point
            print('YES')
            return 'YES'

        if x1>x2:
            gap = distance(dist1, dist2)
        elif x2>x1:
            gap = distance(dist2, dist1)
        
        if gap < init_gap:
            pass
        elif gap >= init_gap:
            print('NO')
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
