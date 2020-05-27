#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dictionary = {}
    for i in range(0,n):
        dictionary[ar[i]] = 0
    for i in range(0,n):
        dictionary[ar[i]] += 1
    print(dictionary.keys())

    pair = 0
    for i in dictionary.keys():
        if not(dictionary[i] % 2):
            count = dictionary[i]/2
            pair += count 
        else:
            count = (dictionary[i]-1)/2
            pair += count
            
    
    return int(pair)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
