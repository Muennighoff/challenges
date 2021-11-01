#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    
    def next_factorial(x):
        if x == 1: return x
        return x * next_factorial(x-1)
    print(next_factorial(n))

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
