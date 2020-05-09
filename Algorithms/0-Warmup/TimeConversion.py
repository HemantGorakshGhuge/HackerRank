#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    list_s = s.split(":")
    hh = int(list_s[0])
    mm = list_s[1]
    ss_format = list_s[2]
    ss = ss_format[:2]
    format_AP = ss_format[2:]
    print(format_AP)
    if format_AP == 'PM':
        if hh == 12:
            hh = 12
        else:
            hh = hh + 12
    elif format_AP == 'AM':
        if hh == 12:
            hh = 0

    if hh < 10:
        hh = '0'+str(hh)
    format_24 = str(hh)+':'+mm+':'+ss
    return format_24
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
