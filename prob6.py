#!/usr/bin/python 

sumsqr=sum([i*i for i in range(1,101)])
sqrsum=sum(range(1,101))
sqrsum*=sqrsum
print sqrsum-sumsqr
