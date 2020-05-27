#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    count_A = 0
    count_O = 0

    for apple in apples:
        dist_Apple=(a+apple)
        if dist_Apple>=s and dist_Apple<=t:
            count_A+=1
        
    for orange in oranges:
        dist_Orange=(b+orange)
        if dist_Orange>=s and dist_Orange<=t:
            count_O+=1
    
    print(count_A)
    print(count_O)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
