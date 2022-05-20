#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazinedict = {}
    for i in magazine:
        if i in magazinedict:
            magazinedict[i]+=1
        else:
            magazinedict[i]=1
    for word in note:
        if word not in magazinedict:
            return "No"
        else:
            magazinedict[word] -= 1
            if magazinedict[word] == 0:
                magazinedict.pop(word)
    return "Yes"
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()
    print(checkMagazine(magazine, note))
