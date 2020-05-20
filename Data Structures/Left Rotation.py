#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    rot = d%n #to reduce additional unimportant rotation
    #Eg:- if 10 rotation and length is 5 then we don't need rotation i.e. rotation = 0

    for _ in range(rot):
        f = a[0]
        a.remove(f)
        a.append(f)

    for i in range(n):
        print(a[i], end=" ")


