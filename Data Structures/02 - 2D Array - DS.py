#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the hourglassSum function below.
def hourglassSum(arr):
    number=1
    dict_matrix={}
    max_sum = -9*6*6
    for j in range(len(arr)-2):
        for i in range(len(arr)-2):
            matrix=[[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
            for x in range(3):
                for y in range(3):
                    matrix[x][y] = arr[i+x][j+y]
            filter_mask = [[1, 1, 1],
                        [0, 1, 0],
                        [1, 1, 1]]
            print(matrix)
            for ii in range(3):
                for jj in range(3):
                    matrix[ii][jj] = matrix[ii][jj] * filter_mask[ii][jj]
            sum_matrix = 0
            print(matrix)
            for xx in range(3):
                for yy in range(3):
                    sum_matrix+=matrix[xx][yy]
            print(sum_matrix)
            max_sum = max(max_sum, sum_matrix)
            print(max_sum)
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
