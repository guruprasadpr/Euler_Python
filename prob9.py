#!/usr/bin/python 

nums=range(1,426)
l1=[i*j*k for i in nums for j in nums for k in nums if (i*i+j*j==k*k and i<j and j<k and i+j+k==1000)]
print l1
print 'Done'
