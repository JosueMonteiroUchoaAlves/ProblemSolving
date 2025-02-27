#!/bin/python

import math
import os
import random
import re
import sys


# write your code here

def avg(*numbers_list):
    numbers = list(numbers_list)
    average = sum(numbers)/ len(numbers)
    return round(average, 2)
num = [1,2,3,4]
res = avg(*num)
print('%.2f' % res + '\n')

