#!/usr/bin/python 

from gprfuncs import *

l1=[sumofdigits(i**j) for i in range(1,100) for j in range(1,100)]
print max(l1)
