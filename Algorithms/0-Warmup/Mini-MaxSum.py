#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total  = sum(arr)

    min_total = total - max(arr)
    max_total = total - min(arr)

    print(str(min_total)+' '+str(max_total))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
