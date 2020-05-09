#!/bin/python3

import math
import os
import random
import re
import sys

def total_sum(arr):
    total_sum = 0
    for i in range(3):
        for j in range(3):
            total_sum += arr[i][j]
    return total_sum

def getCost(list1, list2):
    cost1 = [abs(x1 - x2) for (x1, x2) in zip(list1[0], list2[0])]
    cost2 = [abs(x1 - x2) for (x1, x2) in zip(list1[1], list2[1])]
    cost3 = [abs(x1 - x2) for (x1, x2) in zip(list1[2], list2[2])]
    
    cost = sum(cost1)+sum(cost2)+sum(cost3)
    
    return cost


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    print(s)
    MagicSquare = {}
    MagicSquare[1] = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
    MagicSquare[2] = [[6, 1, 8],[7, 5, 3],[2, 9, 4]]
    MagicSquare[3] = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]
    MagicSquare[4] = [[2, 9, 4],[7, 5, 3],[6, 1, 8]]
    MagicSquare[5] = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
    MagicSquare[6] = [[4, 3, 8],[9, 5, 1],[2, 7, 6]]
    MagicSquare[7] = [[6, 7, 2],[1, 5, 9],[8, 3, 4]]
    MagicSquare[8] = [[2, 7, 6],[9, 5, 1],[4, 3, 8]]
    
    print(MagicSquare)
    cost = {}
    for i in range(8):
        cost[i+1] = getCost(s,MagicSquare[i+1])
    print(cost)

    min_cost_key = min(cost.keys(), key=(lambda k: cost[k]))

    return cost[min_cost_key]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
