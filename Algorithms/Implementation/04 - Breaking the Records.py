#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    score_list = []
    minMax = [0, 0]
    minimum = scores[0]
    maximum = scores[0]
    for i in range(1, len(scores)):
        # score_list.append(score)
        print(scores[i], minimum, maximum)
        if scores[i] < minimum:
            minimum = scores[i]
            minMax[1] += 1
        if scores[i] > maximum:
            maximum = scores[i]
            minMax[0] += 1
    return minMax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
