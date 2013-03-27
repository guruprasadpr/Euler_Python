#!/usr/bin/python 

from gprfuncs import *
from collections import defaultdict

l1=[1]
print 'Beg'
#x= primeFacPow(24)
#d1=defaultdict(int)
#d2=defaultdict(int)
#for i in x:
#        d1[i]+=1
#d2[24]=sum(d1.values())+len(d1)
#print d2[24]
#print 'Done'


for i in range(2,500000): l1.append(l1[-1]+i)
#print l1
for nat in l1:
        lpr= primeFacPow(nat)
        #print lpr
        d1=defaultdict(int)
        for i in lpr:
                d1[i]+=1
        if ((sum(d1.values())+len(d1))>=50):
                print nat
                break

print 'Done'
