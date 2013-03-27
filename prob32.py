#!/usr/bin/python 

def chkFunc(x,y):
    z=x+str(y)
    if len(set(list(z)))==9 and not d1.has_key(y):
            d1[y]=1
            return True
    else:
            return False

d1={}
l1=[i*j for i in range(11,9999) for j in range(11,9999) if chkFunc(str(i)+str(j),i*j)]
#print l1
print sum(l1)
