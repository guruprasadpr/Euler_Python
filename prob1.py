#!/usr/bin/python

def chkval(x):
   return True if (x%3==0 or x%5==0) else False

print sum(filter(chkval,range(1,1000)))
