#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if n%2 and p%2 or not(n%2) and not(p%2): #odd odd or even even
        turn1 = (n-p)/2
        turn2 = p/2

    elif n%2 and not(p%2): #odd even 
        turn1 = ((n-1)-p)/2
        turn2 = p/2

    elif not(n%2) and p%2: #even odd 
        turn1 = (n-(p-1))/2
        turn2 = (p-1)/2
    
    turn = min(turn1, turn2)

    return int(turn)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
