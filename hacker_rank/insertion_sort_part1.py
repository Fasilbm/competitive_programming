#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    n=len(arr)
    val=arr[n-1]
    index1=n-1
    index2=n-2
    for i in range(len(arr)):
        if val<arr[index2] and index2>=0:
            arr[index1]=arr[index2]
            index1-=1
            index2-=1
            print(*arr)
        elif index2>=0:
            arr[index1]=val
            print(*arr)
            break
        else:
            index2==0
            arr[index1]=val
            print(*arr)
            break
            
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
