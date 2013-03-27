#!/usr/bin/python 


def chkPerm(x):
     return True if set(list(str(x))) == set(list(str(x*2))) and set(list(str(x))) == set(list(str(x*3)))and set(list(str(x))) == set(list(str(x*4)))and set(list(str(x))) == set(list(str(x*5))) and set(list(str(x))) == set(list(str(x*6))) else False

print filter(chkPerm,range(100001,200000))
