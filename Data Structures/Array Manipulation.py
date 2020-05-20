#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    m = len(queries)
    print(n, m, queries)
    arr = [0 for col in range(n)]

    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        arr[a-1] += k
        if b < n:
            arr[b] -= k
    
    max_sum = s = 0

    for i in arr:
        s += i
        max_sum = max(max_sum, s)
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
