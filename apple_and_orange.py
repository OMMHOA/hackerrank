#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def count_elements_in_range(elements, min_value, max_value):
    count = 0
    for e in elements:
        if e >= min_value and e <= max_value:
            count += 1
    return count

    
def count_elements_in_range2(elements, min_value, max_value):
    is_element_in_range = lambda e: e >= min_value and e <= max_value
    return len(list(filter(is_element_in_range, elements)))
    
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_min_d = s - a
    apple_max_d = t - a
    apples_on_house = count_elements_in_range(apples, apple_min_d, apple_max_d)
    
    orange_min_d = s - b
    orange_max_d = t - b
    oranges_on_house = count_elements_in_range2(oranges, orange_min_d, orange_max_d)
    
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
