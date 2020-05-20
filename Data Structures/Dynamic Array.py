#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    S={}
    for i in range(n):
        S[i]=[]
    lastAnswer_list = []
    for query in queries:
        a = query[0]
        x = query[1]
        y = query[2]
        index  = ((x^lastAnswer)%n)
        seq = S[index]
        if a==1:
            seq.append(y)
        elif a==2:
            size = len(seq)
            lastAnswer=seq[y%size]
            lastAnswer_list.append(lastAnswer)
    
    return lastAnswer_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
