#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(A):
    # Write your code here

    # Compute the surface where blocks touch
    # Two types: Side-touch; Above/bottom touch
    total_touch = 0
    total_blocks = 0
    rows = len(A)
    for i in range(rows):
        cols = len(A[i])
        for j in range(cols):
            height_cur = A[i][j]
            # Above/bottom
            # If 1: 0; 2: 2; 3: 4; 4: 6
            above_bott_touch = (height_cur - 1) * 2
            # Sides
            side_touch = 0
            if j + 1 < cols:
                height_r = A[i][j + 1]
                side_touch += min(height_r, height_cur)
            if j - 1 >= 0:
                height_l = A[i][j - 1]
                side_touch += min(height_l, height_cur)
            if i + 1 < rows:
                height_b = A[i + 1][j]
                side_touch += min(height_b, height_cur)
            if i - 1 >= 0:
                height_t = A[i - 1][j]
                side_touch += min(height_t, height_cur)
            total_touch += above_bott_touch + side_touch
            total_blocks += height_cur * 6
    return total_blocks - total_touch

    # total surface - above to get free surface


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + "\n")

    fptr.close()
